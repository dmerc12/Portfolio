from user.forms import LoginForm, EditUserForm, ChangePasswordForm
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

    ## Tests for edit user form
    ### Test edit user form initialization
    def test_edit_user_form_initialization(self):
        form = EditUserForm()
        self.assertIn('username', form.fields.keys())
        self.assertIn('first_name', form.fields.keys())
        self.assertIn('last_name', form.fields.keys())
        self.assertIn('email', form.fields.keys())
        self.assertIn('phone_number', form.fields.keys())

    ### Test edit user form validation with empty fields
    def test_edit_user_form_validation_empty_fields(self):
        data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'phone_number': '',
        }
        form = EditUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test edit user form validation with fields too long
    def test_edit_user_form_validation_fields_too_long(self):
        data = {
            'username': 'test' * 50,
            'first_name': 'test' * 50,
            'last_name': 'test' * 50,
            'email': 'test' * 50 + '@email.com',
            'phone_number': '1' * 16,
        }
        form = EditUserForm(data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('username', form.errors)
        self.assertIn('first_name', form.errors)
        self.assertIn('last_name', form.errors)
        self.assertIn('email', form.errors)
        self.assertIn('phone_number', form.errors)

    ### Test edit user form validation with invalid email
    def test_edit_user_form_validation_invalid_email(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'incorrect format',
            'phone_number': '1-123-123-1234'
        }
        form = EditUserForm(data=data)
        self.assertIn('email', form.errors)

    ### Test edit user form validation success
    def test_edit_user_form_validation_success(self):
        data = {
            'username': 'test',
            'first_name': 'test',
            'last_name': 'test',
            'email': 'test@email.com',
            'phone_number': '1-123-123-1234'
        }
        form = EditUserForm(data=data)
        self.assertTrue(form.is_valid())

    ## Tests for change password form
    ### Test change password form initialization
    def test_change_password_form_initialization(self):
        base = User.objects.create_user(username='username', password='testpass123', first_name='user', last_name='name', email='test@email.com')
        form = ChangePasswordForm(user=base)
        self.assertIn('new_password1', form.fields.keys())
        self.assertIn('new_password2', form.fields.keys())

    ### Test change password form validation with empty fields
    def test_change_password_form_validation_empty_fields(self):
        data = {'new_password1': '', 'new_password2': ''}
        base = User.objects.create_user(username='username', password='testpass123', first_name='user', last_name='name', email='test@email.com')
        form = ChangePasswordForm(user=base, data=data)
        self.assertIn('new_password1', form.errors)
        self.assertIn('new_password2', form.errors)

    ### Test change password form validation with an invalid password
    def test_change_password_form_validation_invalid_password(self):
        base = User.objects.create_user(username='username', password='testpass123', first_name='user', last_name='name', email='test@email.com')
        data = {'new_password1': base.first_name, 'new_password2': base.first_name}
        form = ChangePasswordForm(user=base, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    ### Test change password form validation with mismatching passwords
    def test_change_password_form_validation_mismatching_passwords(self):
        data = {'new_password1': 'mismatching', 'new_password2': 'passwords'}
        base = User.objects.create_user(username='username', password='testpass123', first_name='user', last_name='name', email='test@email.com')
        form = ChangePasswordForm(user=base, data=data)
        self.assertFalse(form.is_valid())
        self.assertIn('new_password2', form.errors)

    ### Test change password form validation success
    def test_change_password_form_validation_success(self):
        data = {'new_password1': 'updatedpass123', 'new_password2': 'updatedpass123'}
        base = User.objects.create_user(username='username', password='testpass123', first_name='user', last_name='name', email='test@email.com')
        form = ChangePasswordForm(user=base, data=data)
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

    ### Test login view success
    def test_login_view_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        data = {'username': user.username, 'password': 'pass12345'}
        response = self.client.post(reverse('login'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f'Welcome {user.first_name} {user.last_name}!', messages)

    ## Tests for logout view
    ### Test logout view success
    def test_logout_view_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(user)
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Goodbye!', messages)

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

    ## Tests for edit user view
    ### Test edit user vew redirect
    def test_edit_user_view_redirect(self):
        response = self.client.get(reverse('edit-user'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    ### Test edit user view rendering success
    def test_edit_user_view_rendering_success(self):
        base = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(base)
        response = self.client.get(reverse('edit-user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/edit.html')
        self.assertIsInstance(response.context['form'], EditUserForm)

    ### Test edit user view success
    def test_edit_user_view_success(self):
        base = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(base)
        data = {
            'username': 'updated',
            'first_name': 'updated',
            'last_name': 'updated',
            'email': 'updated@email.com',
            'phone_number': '1-111-111-1111'
        }
        response = self.client.post(reverse('edit-user'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        self.assertTrue(User.objects.filter(username=data['username']).exists())
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Information successfully edited!", messages)

    ## Tests for change password view
    ### Test change password view redirect
    def test_change_password_redirect(self):
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))

    ### Test change password view rendering success
    def test_change_password_view_rendering_success(self):
        base = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(base)
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user/change-password.html')
        self.assertIsInstance(response.context['form'], ChangePasswordForm)

    ### Test change password view success
    def test_change_password_success(self):
        base = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(base)
        data = {
            'new_password1': 'new12345',
            'new_password2': 'new12345'
        }
        response = self.client.post(reverse('change-password'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('home'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"Password successfully changed!", messages)
