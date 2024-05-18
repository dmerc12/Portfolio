from rest_framework import serializers
from contact.models import Contact

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['first_name', 'last_name', 'phone_number', 'email', 'subject', 'message']
