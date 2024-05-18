from contact.views import contact, contact_home, mark_response, delete_contact
from django.urls import path

urlpatterns = [
    path('', contact, name='contact'),
    path('home/', contact_home, name='contact-home'),
    path('delete/<int:contact_id>/', delete_contact, name='delete-contact'),
    path('mark-response/<int:contact_id>/', mark_response, name='mark-response'),
]
