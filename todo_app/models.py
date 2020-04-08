from django.db import models
from django import forms
from django.utils.text import slugify
# Create your models here.
class Item(models.Model):
    text = models.CharField(max_length=30)
    slug = models.SlugField(unique=True, allow_unicode=True, editable=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

    def remove(self):
        self.delete()
        
    def save(self):
        self.slug = slugify(self.text)
        self.text = self.text.title()
        return super().save()

    class Meta:
        ordering = ['-date_created']

