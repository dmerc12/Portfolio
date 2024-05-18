from project.views import project_home, add_project
from django.urls import path

urlpatterns = [
    path('home/', project_home, name='project-home'),
    path('add/', add_project, name='add-project'),
]
