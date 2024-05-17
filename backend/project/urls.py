from project.views import project_home
from django.urls import path

urlpatterns = [
    path('home/', project_home, name='project-home'),
]
