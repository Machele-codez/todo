from django.contrib import admin
from .models import Task, User
from django.contrib.auth import get_user_model
# Register your models here.

class TaskInline(admin.StackedInline):
    model = Task
    extra = 1
class UserAdmin(admin.ModelAdmin):
    model = User
    inlines = [
        TaskInline,
    ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Task)