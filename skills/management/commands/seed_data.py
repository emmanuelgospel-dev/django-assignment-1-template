from django.core.management.base import BaseCommand
from skills.models import Skill
from blog.models import BlogPost


class Command(BaseCommand):
    help = "Seed sample skills and blog posts for local development."

    def handle(self, *args, **options):
        skills_data = [
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
        for data in skills_data:
            _, created = Skill.objects.get_or_create(name=data["name"], defaults=data)
            if created:
                created_skills += 1

        posts_data = [
            {
                "title": "Why I build things that solve real problems",
                "category": "product",
                "content": (
                    "I don't build to experiment. I build because something is broken and I can fix it. "
                    "This post is about the mindset shift from tinkering to shipping — and why purpose-driven "
                    "building compounds faster than curiosity-driven building ever will."
                ),
            },
            {
                "title": "Django ownership patterns: ForeignKey to User, done right",
                "category": "engineering",
                "content": (
                    "A walkthrough of task/post ownership in Django using ForeignKey relationships to the "
                    "built-in User model, covering login_required decorators, instance-based form reuse for "
                    "edit views, and the common pitfalls that trip up beginners."
                ),
            },
            {
                "title": "Designing like Linear when you're a solo developer",
                "category": "design",
                "content": (
                    "Notes on applying premium design language — glassmorphism, restrained accent color, "
                    "intentional typography — to a portfolio site built by one person with no design team. "
                    "What to steal from Apple, Linear, and Arc, and what to leave behind."
                ),
            },
        ]
        created_posts = 0
        for data in posts_data:
            _, created = BlogPost.objects.get_or_create(title=data["title"], defaults=data)
            if created:
                created_posts += 1

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {created_skills} new skills and {created_posts} new blog posts."
        ))
