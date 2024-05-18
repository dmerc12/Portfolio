from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.staticfiles.finders import find
from django.contrib.messages import get_messages
from django.contrib.auth.models import User
from django.test import TestCase, Client
from project.forms import ProjectForm
from project.models import Project
from django.urls import reverse

# Tests for project model
class TestProjectModel(TestCase):

    ## Test project string method
    def test_project_str(self):
        project = Project.objects.create(title='title', thumbnail='test/path.png', repo='https://test.com/')
        self.assertEqual(str(project), f'PRO{project.pk} - {project.title}')

    ## Test for image preview method
    def test_image_preview(self):
        project = Project.objects.create(title='title', thumbnail='test/path.png', repo='https://test.com/')
        preview = project.image_preview()
        self.assertEqual(preview, f'<img src="{project.thumbnail.url}" style="max-width:200px; max-height: 200px"/>')

# Tests for project form
class TestProjectForm(TestCase):

    ## Test project form initialization
    def test_project_form_initialization(self):
        form = ProjectForm()
        self.assertIn('title', form.fields.keys())
        self.assertIn('thumbnail', form.fields.keys())
        self.assertIn('repo', form.fields.keys())
        self.assertIn('demo', form.fields.keys())

    ## Test project form validation with empty inputs
    def test_project_form_validation_empty_inputs(self):
        files = {
            'thumbnail': ''
        }
        data = {
            'title': '',
            'repo': '',
            'demo': ''
        }
        form = ProjectForm(data=data, files=files)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('thumbnail', form.errors)
        self.assertIn('repo', form.errors)

    ## Test project form validation with fields too long
    def test_project_form_validation_fields_too_long(self):
        files = {
            'thumbnail': SimpleUploadedFile(name='finance.png', content=open(find('finance.png'), 'rb').read(), content_type='image/png')
        }
        data = {
            'title': 't' * 101,
            'repo': 't' * 301,
            'demo': 't' * 301
        }
        form = ProjectForm(data=data, files=files)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)
        self.assertIn('repo', form.errors)
        self.assertIn('demo', form.errors)

    ## Test project form validation success
    def test_project_form_validation_success(self):
        files = {
            'thumbnail': SimpleUploadedFile(name='finance.png', content=open(find('finance.png'), 'rb').read(), content_type='image/png')
        }
        data = {
            'title': 'title',
            'repo': 'test/repo.com',
            'demo': 'test/demo.com'
        }
        form = ProjectForm(data=data, files=files)
        self.assertTrue(form.is_valid())

class TestProjectViews(TestCase):

    def setUp(self):
        self.client = Client()

    ## Tests for project home view
    ### Test project home view redirect
    def test_project_home_view_redirect(self):
        response = self.client.get(reverse('project-home'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn(f"You must be a site admin to access this page!", messages)

    ### Test project home view rendering success
    def test_project_home_view_rendering_success(self):
        user = User.objects.create_user(username='adminuser', password='pass12345', first_name='admin', last_name='admin', email='admin@email.com')
        self.client.force_login(user)
        response = self.client.get(reverse('project-home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/home.html')

     ## Tests for add project view
    ### Test add project view redirect
    def test_add_project_view_redirect(self):
        response = self.client.get(reverse('add-project'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('login'))
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('You must be a site admin to access this page!', messages)

    ### Test add project view rendering success
    def test_add_project_view_rendering_success(self):
        base = User.objects.create(username='test', password='test', first_name='first', last_name='last', email='firstlast@email.com')
        self.client.force_login(base)
        response = self.client.get(reverse('add-project'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'project/create.html')
        self.assertIsInstance(response.context['form'], ProjectForm)

    ### Test add project view success
    def test_add_project_view_success(self):
        base = User.objects.create(username='test', password='test', first_name='first', last_name='last', email='firstlast@email.com')
        self.client.force_login(base)
        data = {
            'title': 'title',
            'thumbnail': SimpleUploadedFile(name='finance.png', content=open(find('finance.png'), 'rb').read(), content_type='image/png'),
            'repo': 'test/repo.com',
            'demo': ''
        }
        response = self.client.post(reverse('add-project'), data=data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('project-home'))
        self.assertTrue(Project.objects.filter(title=data['title']).exists())
        messages = [message.message for message in get_messages(response.wsgi_request)]
        self.assertIn('Project successfully added!', messages)
