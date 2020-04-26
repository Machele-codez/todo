from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model
import datetime
from django import forms

# Create your models here.

User = get_user_model()


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    text = models.CharField(max_length=30)
    date_created = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=False)
    completed_on = models.DateTimeField(blank=True, null=True)
    # CRITICAL = 'A'; HIGH = 'B'; MODERATE = 'C'; LOW = 'D'
    PRIORITY_CHOICES = [
    ('A', 'critical'),
    ('B', 'high'),
    ('C', 'moderate'),
    ('D', 'low'),
    ]
    priority = models.CharField(max_length=15, choices=PRIORITY_CHOICES)
    # get a field that would be the appended value of the input date and input time to be the final due_datetime
    due_datetime = models.DateTimeField(blank=True, null=True)
    


    #// def complete(self):
    #//    self.completed = True
    #//     self.completed_on = datetime.datetime.now()
    #//     self.save()

    def __str__(self):
        return f"{self.text} | {self.user}".title()

    def remove(self):
        self.delete()
        
    def save(self):
        self.text = self.text.title()
        return super().save()

    class Meta:
        ordering = ['-date_created']
        
        #TODO: to make sure that each task and user taken together is unique
        constraints = [
            models.UniqueConstraint(fields=['user', 'text'], name='unique_user_task'),
        ]