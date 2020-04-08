from django.db import models
from django.utils.text import slugify
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    text = models.CharField(max_length=30)
    # slug = models.SlugField(allow_unicode=True, editable=False)
    date_created = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text

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