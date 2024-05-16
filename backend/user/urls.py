from user.views import home, login_user
from django.urls import path

urlpatterns = [
    path('login/', login_user, name='login'),
    path('home/', home, name='home'),
]
