# Generated by Django 2.2.7 on 2020-04-11 03:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0014_task_priority'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='status',
        ),
    ]