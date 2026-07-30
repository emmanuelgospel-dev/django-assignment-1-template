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
                "title": 'I Stopped Asking "Can I Build It?" and Started Asking "Should I?"',
                "category": "product",
                "content": """When I started learning software development, I thought good projects were the ones with the most features.

The more complicated the app, the more impressive it looked.

Lately, my thinking has changed.

I've started caring less about building everything and more about solving one real problem well.

That mindset became even clearer while working on a healthcare coordination project.

We realised people don't just need the nearest hospital.

They need the nearest hospital that can actually treat them.

That single observation changed the direction of the project.

It reminded me that software isn't valuable because it's complex.

It's valuable because it helps someone.

These days, before I start building anything, I try to ask myself one question.

If this didn't exist tomorrow, who would actually miss it?

If I can't answer that, then maybe I should keep thinking before I start coding.

I'd rather build fewer projects that matter than a hundred that don't.
"""
            },

            {
                "title": "Designing With Intention Instead of Decoration",
                "category": "design",
                "content": """When I first started designing websites, I loved making things look impressive.

More shadows.
More gradients.
More animations.

If a design looked busy, I felt like I had done a good job.

The funny thing is, I already knew the principle that less is more. I came from a graphic design background, so it wasn't a new idea. But knowing a principle and actually applying it are two different things.

Building this portfolio reminded me of that.

Every time I wanted to add another effect, I stopped and asked myself one question.

Does this make the experience better, or am I decorating it because I can?

Most times, the answer was the second one.

So I removed things.

I kept one accent color.

I gave the content room to breathe.

I paid more attention to spacing than special effects.

The goal stopped being to impress people.

The goal became helping people focus on what matters.

Good design isn't about how much you can add.

It's about knowing what deserves to stay.
"""
            },

            {
                "title": "I Finally Understood Why Django Uses ForeignKey for Users",
                "category": "engineering",
                "content": """One thing that kept confusing me while learning Django was this:

Why do tutorials always connect things like posts and tasks to the User model using a ForeignKey?

Why not just save the username?

At first, both approaches looked the same to me.

Then it finally clicked.

A username is just text.

A User object is an actual person inside your application.

If I save the username and someone changes it later, that relationship starts falling apart.

But when I connect a blog post to the User model with a ForeignKey, Django keeps that ownership intact even if the username or email changes.

That's when I stopped seeing ForeignKey as just another thing to memorize.

It's about relationships.

Ownership.

Keeping your data connected the right way.

That small lesson changed how I look at database design, and now I find myself asking a different question whenever I build something:

What should this belong to?

Sometimes understanding the reason behind the code is worth more than memorizing the syntax.
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