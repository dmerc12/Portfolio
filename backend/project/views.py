from django.shortcuts import render, redirect, get_object_or_404
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
