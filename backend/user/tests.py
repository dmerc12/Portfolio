from user.forms import LoginForm
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse

# Tests for users forms
class TestUsersForms(TestCase):

    ## Tests for login form
    ### Test for login form initialization
    def test_login_form_initialization(self):
        form = LoginForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('password', form.fields.keys())

    ### Test for login form validation with empty fields
    def test_login_form_validation_empty_fields(self):
        data = {'username': '', 'password': ''}
        form = LoginForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('password', form.errors)

    ### Test login form validation success
    def test_login_form_validation_success(self):
        data = {'username': 'username', 'password': 'password'}
        form = LoginForm(data=data)
        self.assertTrue(form.is_valid())

# Tests for users views
class TestUsersViews(TestCase):

    def setUp(self):
        self.client = Client()

    ## Tests for login view
    ### Test login view rendering success
    def test_login_view_rendering_success(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/login.html')
        self.assertIsInstance(response.context['form'], LoginForm)

    ### Test login view with incorrect credentials
    def test_login_view_incorrect_credentials(self):
        data = {'username': 'incorrect', 'password': 'credentials'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 200)
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Incorrect username or password, please try again!', messages)

    ### Test login view success with admin
    def test_login_view_admin_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        data = {'username': user.username, 'password': 'pass12345'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'Welcome {user.first_name} {user.last_name}!', messages)

    ## Tests for admin home
    ### Test for admin home redirect
    def test_admin_home_redirect(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin to access this page!', messages)

    ### Test for admin home rendering success
    def test_admin_home_rendering_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(user)
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/home.html')
