from django.utils.html import format_html
from django.db import models

# Model for project
class Project(models.Model):
    title =  models.CharField(max_length=100)
    thumbnail = models.ImageField(upload_to='media/inventory/designs/')
    repo = models.CharField(max_length=300)
    demo = models.CharField(max_length=300, default='')
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'PRO{self.pk} - {self.title}'

    def image_preview(self):
        return format_html(f'<img src="{self.thumbnail.url}" style="max-width:200px; max-height: 200px"/>')
