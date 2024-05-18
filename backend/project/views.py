from django.shortcuts import render, redirect, get_object_or_404
from project.forms import ProjectForm
from django.contrib import messages
from project.models import Project

# Project home view
def project_home(request):
    if request.user.is_authenticated:
        projects = Project.objects.all()
        return render(request, 'project/home.html', {'projects': projects})
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')

# Add project view
def add_project(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ProjectForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Project successfully added!')
                return redirect('project-home')
        else:
            form = ProjectForm()
        return render(request, 'project/create.html', {'form': form})
    else:
        messages.error(request, 'You must be a site admin to access this page!')
        return redirect('login')
