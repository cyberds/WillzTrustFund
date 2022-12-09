from django.shortcuts import render, redirect, get_object_or_404
from company.models import Company
from .models import Program, Project, Activity, ActivityImage
# Create your views here.

def program(request, id):
    program = get_object_or_404(Program, id=id)
    projects= Project.objects.filter(program=program)[:3]
    activities = Activity.objects.filter(program=program)[:3]

    project_desc = {}
    for project in projects:
        project_desc[project.id] = ' '.join(project.project_description.split(' ')[:50]) + '...'

    activity_desc = {}
    for activity in activities:
        activity_desc[activity.id] = ' '.join(activity.activity_description.split(' ')[:25]) + '...'

    context = {
        'program': program,
        'projects': projects,
        'project_desc': project_desc,
        'activity_desc': activity_desc,
        'activities': activities,
    }

    return render(request, 'program.html', context)

def project(request, id):
    project = get_object_or_404(Project, id=id)
    activities = Activity.objects.filter(project=project)[:3]

    display_desc = {}
    for activity in activities:
        display_desc[activity.id] = ' '.join(activity.activity_description.split(' ')[:50]) + '...'

    context = {
        'project': project,
        'activities': activities,
        'display_desc': display_desc,
    }
    return render(request, 'project.html', context)

def activity(request, id):
    activity = get_object_or_404(Activity, id=id)
    activity_images = ActivityImage.objects.filter(activity=activity)


    context = {
        'activity': activity,
        'activity_images': activity_images,
    }
    return render(request, 'activity.html', context)
