from contact.serializers import ContactSerializer
from django.test import TestCase, Client
from contact.models import Contact
from django.urls import reverse

# Tests for contact model
class TestContactModel(TestCase):

    ### Test contact string method
    def test_contact_str(self):
        contact = Contact.objects.create(first_name='test', last_name='test', phone_number='1-123-123-1234', email='test@email.com', subject='subject', message='message')
        self.assertEqual(str(contact), f'{contact.first_name} {contact.last_name} - {contact.subject}')

# Tests for contact serializer
class TestContactSerializer(TestCase):

    ### Test serializer with valid data
    def test_serializer_valid_data(self):
        valid_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'email': 'john@example.com',
            'subject': 'Test Subject',
            'message': 'Test Message'
        }
        serializer = ContactSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())

    ### Test serializer with invalid data
    def test_serializer_invalid_data(self):
        invalid_data = {
            'first_name': 't' * 101,
            'last_name': 't' * 101,
            'phone_number': 't' * 16,
            'email': 't' * 251,
            'subject': 't' * 251,
            'message': 't' * 501
        }
        serializer = ContactSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('first_name', serializer.errors)
        self.assertIn('last_name', serializer.errors)
        self.assertIn('phone_number', serializer.errors)
        self.assertIn('email', serializer.errors)
        self.assertIn('subject', serializer.errors)
        self.assertIn('message', serializer.errors)

# Tests for contact views
class TestContactViews(TestCase):

    def setUp(self):
        self.client = Client()

    ## Tests for contact view
    ### Test contact view with fields too long
    def test_contact_view_fields_too_long(self):
        data = {
            'first_name': 't' * 101,
            'last_name': 't' * 101,
            'phone_number': 't' * 16,
            'email': 't' * 251,
            'subject': 't' * 251,
            'message': 't' * 501
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('first_name', response.json())
        self.assertIn('last_name', response.json())
        self.assertIn('phone_number', response.json())
        self.assertIn('email', response.json())
        self.assertIn('subject', response.json())
        self.assertIn('message', response.json())

    ### Test contact view success
    def test_contact_view_success(self):
        data = {
            'first_name': 'first',
            'last_name': 'last',
            'phone_number': '1-234-456-7890',
            'email': 'test@email.com',
            'subject': 'subject',
            'message': 'message'
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['message'], 'Form successfully submitted. I will be in contact soon!')
