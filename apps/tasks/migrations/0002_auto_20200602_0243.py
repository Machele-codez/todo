# Generated by Django 2.2.7 on 2020-06-02 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='task',
            name='unique_user_task',
        ),
    ]
