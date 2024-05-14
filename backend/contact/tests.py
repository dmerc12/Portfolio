from django.test import TestCase, Client
from contact.models import Contact
from django.urls import reverse

# Tests for contact models
class TestContactModels(TestCase):

    ## Tests for contact model
    ### Test contact string method
    def test_contact_str(self):
        contact = Contact.objects.create(first_name='test', last_name='test', phone_number='1-123-123-1234', email='test@email.com', subject='subject', message='message')
        self.assertEqual(str(contact), f'{contact.first_name} {contact.last_name} - {contact.subject}')

# Tests for contact views
class TestContactViews(TestCase):

    def setUp(self):
        self.client = Client()

    ## Tests for contact view
    ### Test contact view with empty fields
    def test_contact_view_empty_fields(self):
        data = {
            'first_name': '',
            'last_name': '',
            'phone_number': '',
            'email': '',
            'subject': '',
            'message': ''
        }
        response = self.client.post(reverse('contact'), data=data)
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()['errors']['first_name'], 'First name is required')
        self.assertEqual(response.json()['errors']['last_name'], 'Last name is required')
        self.assertEqual(response.json()['errors']['phone_number'], 'Phone number is required')
        self.assertEqual(response.json()['errors']['email'], 'Email is required')
        self.assertEqual(response.json()['errors']['subject'], 'Subject is required')
        self.assertEqual(response.json()['errors']['message'], 'Message is required')

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
        self.assertEqual(response.status_code, 422)
        self.assertEqual(response.json()['errors']['first_name'], 'First name cannot exceed 100 characters')
        self.assertEqual(response.json()['errors']['last_name'], 'Last name cannot exceed 100 characters')
        self.assertEqual(response.json()['errors']['phone_number'], 'Phone number cannot exceed 15 characters')
        self.assertEqual(response.json()['errors']['email'], 'Email cannot exceed 250 characters')
        self.assertEqual(response.json()['errors']['subject'], 'Subject cannot exceed 250 characters')
        self.assertEqual(response.json()['errors']['message'], 'Message cannot exceed 500 characters')

    ### Test contact view with incorrect HTTP method
    def test_contact_view_incorrect_http_method(self):
        response = self.client.get(reverse('contact'))
        self.assertEqual(response.status_code, 403)
        self.assertEqual(response.json()['error'], 'Invalid HTTP method')

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
        self.assertEqual(response.json()['message'], 'Submitted successfully, I will be in contact soon!')
