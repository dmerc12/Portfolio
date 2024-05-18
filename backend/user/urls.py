from user.views import login_user, logout_user, edit_user, change_password
from django.urls import path

urlpatterns = [
    path('', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit/', edit_user, name='edit-user'),
    path('change-password/', change_password, name='change-password'),
]
