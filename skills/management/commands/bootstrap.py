import os

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from skills.models import Skill
from blog.models import BlogPost
from django.utils.text import slugify


class Command(BaseCommand):
    help = "Bootstrap the application with initial data."

    def handle(self, *args, **options):

        # ----------------------------
        # Create Superuser
        # ----------------------------

        User = get_user_model()

        username = os.getenv("DJANGO_SUPERUSER_USERNAME")
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")

        if username and email and password:

            if not User.objects.filter(username=username).exists():

                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password,
                )

                self.stdout.write(
                    self.style.SUCCESS("✓ Superuser created.")
                )

            else:

                self.stdout.write(
                    self.style.WARNING("✓ Superuser already exists.")
                )

        else:

            self.stdout.write(
                self.style.WARNING(
                    "Superuser environment variables not found. Skipping..."
                )
            )

        # ----------------------------
        # Skills
        # ----------------------------

        skills = [
            {"name": "Python", "category": "backend", "proficiency": 75, "order": 1},
            {"name": "Django", "category": "backend", "proficiency": 65, "order": 2},
            {"name": "PHP / MySQL", "category": "backend", "proficiency": 60, "order": 3},
            {"name": "JavaScript", "category": "frontend", "proficiency": 70, "order": 4},
            {"name": "HTML / CSS", "category": "frontend", "proficiency": 85, "order": 5},
            {"name": "Tailwind CSS", "category": "frontend", "proficiency": 75, "order": 6},
            {"name": "CorelDraw", "category": "design", "proficiency": 90, "order": 7},
            {"name": "UI Design", "category": "design", "proficiency": 70, "order": 8},
            {"name": "Git / GitHub", "category": "tools", "proficiency": 65, "order": 9, "is_tool": True},
            {"name": "VS Code", "category": "tools", "proficiency": 90, "order": 10, "is_tool": True},
        ]

        created_skills = 0

        for skill in skills:

            _, created = Skill.objects.get_or_create(
                name=skill["name"],
                defaults=skill,
            )

            if created:
                created_skills += 1

        # ----------------------------
        # Blog Posts
        # ----------------------------

        posts = [

            {
                "title": "Why I Build Things That Solve Real Problems",
                "category": "product",
                "content": """Most people build projects to learn.

I build projects to solve problems.

Every portfolio project I create starts with a real frustration I experienced or observed.

That changes everything.

Instead of chasing technologies, I focus on building products people can actually use.

The code is important.

But solving the right problem matters even more.
"""
            },

            {
                "title": "Designing with Intention",
                "category": "design",
                "content": """Good design isn't decoration.

It's communication.

Every spacing decision, font size, animation and colour should have a reason.

Minimal interfaces aren't empty because they're trendy.

They're minimal because they remove distractions and help people focus on what matters.

Less isn't boring.

Less is intentional.
"""
            },

            {
                "title": "Understanding Django Ownership Patterns",
                "category": "engineering",
                "content": """One of the biggest lessons I learnt in Django was ownership.

Instead of every user editing every object, each object belongs to someone.

Using ForeignKey relationships with Django's User model makes permissions much easier to manage.

It's a simple concept that scales surprisingly well.
"""
            },

        ]

        created_posts = 0

        for post in posts:

            defaults = post.copy()
            defaults["slug"] = slugify(post["title"])

            _, created = BlogPost.objects.get_or_create(
                title=post["title"],
                defaults=defaults,
            )

            if created:
                created_posts += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nBootstrap complete!\n"
                f"Skills created: {created_skills}\n"
                f"Posts created: {created_posts}"
            )
        )