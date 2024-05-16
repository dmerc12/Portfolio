from contact.serializers import ContactSerializer
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
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

    ## Tests for contact home view
    ### Test contact home view redirect
    def test_contact_home_view_redirect(self):
        response = self.client.get(reverse('contact-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"You must be a site admin to access this page!", messages)

    ### Test contact home view rendering success
    def test_contact_home_view_rendering_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(user)
        response = self.client.get(reverse('contact-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/home.html')

    ## Tests for mark response view
    ### Test mark response view redirect
    def test_mark_response_view_redirect(self):
        contact = Contact.objects.create(first_name='first', last_name='last', phone_number='1-123-456-7890', email='e@mail.com', subject='subject', message='message')
        response = self.client.get(reverse('mark-response', args=[contact.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"You must be a site admin to access this page!", messages)

    ### Test mark response view success already responded
    def test_mark_response_view_success_already_responded(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        contact = Contact.objects.create(first_name='first', last_name='last', phone_number='1-123-456-7890', email='e@mail.com', subject='subject', message='message', responded=True)
        self.client.force_login(user)
        response = self.client.get(reverse('mark-response', args=[contact.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Response noted!", messages)

    ### Test mark response view success
    def test_mark_response_view_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        contact = Contact.objects.create(first_name='first', last_name='last', phone_number='1-123-456-7890', email='e@mail.com', subject='subject', message='message')
        self.client.force_login(user)
        response = self.client.get(reverse('mark-response', args=[contact.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact-home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Response noted!", messages)

    ## Tests for delete contact view
    ### Test delete contact view redirect
    def test_delete_contact_view_redirect(self):
        contact = Contact.objects.create(first_name='first', last_name='last', phone_number='1-123-456-7890', email='e@mail.com', subject='subject', message='message')
        response = self.client.get(reverse('delete-contact', args=[contact.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"You must be a site admin to access this page!", messages)

    ### Test delete contact view rendering success
    def test_change_password_view_rendering_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        contact = Contact.objects.create(first_name='first', last_name='last', phone_number='1-123-456-7890', email='e@mail.com', subject='subject', message='message')
        self.client.force_login(user)
        response = self.client.get(reverse('delete-contact', args=[contact.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'contact/delete.html')

    ### Test delete contact view success
    def test_delete_contact_view_success(self):
        contact = Contact.objects.create(first_name='first', last_name='last', phone_number='1-123-456-7890', email='e@mail.com', subject='subject', message='message')
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(user)
        response = self.client.post(reverse('delete-contact', args=[contact.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('contact-home'))
        self.assertFalse(Contact.objects.filter(pk=contact.pk).exists())
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Message successfully deleted!", messages)
