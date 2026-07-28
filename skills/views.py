from django.shortcuts import render
from .models import Skill


def skill_list(request):
    skills = Skill.objects.filter(is_tool=False).order_by('order')
    tools = Skill.objects.filter(is_tool=True).order_by('order')
    context = {
        'skills': skills,
        'tools': tools,
    }
    return render(request, 'skills/skill_list.html', context)
