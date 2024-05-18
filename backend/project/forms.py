from project.models import Project
from django import forms

# Project form
class ProjectForm(forms.ModelForm):
    title = forms.CharField(label='Project Title', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a title for the project'}))
    thumbnail = forms.ImageField(label='Project Thumbnail')
    repo = forms.CharField(label='Project Code Repository', max_length=300, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the URL to the project\'s code repository'}))
    demo = forms.CharField(label='Project Live Demo', max_length=300, required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the URL to the project\'s live demo once deployed'}))

    class Meta:
        model = Project
        fields = ['title', 'thumbnail', 'repo', 'demo']
