from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import datetime
# Create your models here.

User = get_user_model()

PRIORITY_CHOICES = [
    ('critical', 'critical'),
    ('high', 'high'),
    ('moderate', 'moderate'),
    ('low', 'low'),
]

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    text = models.CharField(max_length=30)
    # slug = models.SlugField(allow_unicode=True, editable=False)
    date_created = models.DateTimeField(auto_now=True)
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    completed = models.BooleanField()
    completed_on = models.DateTimeField()

    def complete(self):
        self.completed = True
        self.date_completed = datetime.datetime.now()

    def __str__(self):
        return f"{self.text} | {self.user}".title()

    def remove(self):
        self.delete()
        
    def save(self):
        # self.slug = slugify(self.text)
        self.text = self.text.title()
        return super().save()

    class Meta:
        ordering = ['-date_created']
        constraints = [
            models.UniqueConstraint(fields=['user', 'text'], name='unique_user_task'),
        ]