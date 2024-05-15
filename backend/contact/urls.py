from contact.views import contact, get_csrf_token
from django.urls import path

urlpatterns = [
    path('', contact, name='contact'),
    path('get_csrf_token/', get_csrf_token, name='get_csrf_token'),
]
