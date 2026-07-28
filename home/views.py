from django.shortcuts import render
from skills.models import Skill
from blog.models import BlogPost


def home(request):
    featured_skills = Skill.objects.order_by('order')[:6]
    latest_posts = BlogPost.objects.order_by('-created_at')[:3]
    context = {
        'featured_skills': featured_skills,
        'latest_posts': latest_posts,
    }
    return render(request, 'home/home.html', context)
