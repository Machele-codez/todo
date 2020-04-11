# Generated by Django 2.2.7 on 2020-04-10 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0011_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(blank=True, choices=[('critical', 'critical'), ('high', 'high'), ('moderate', 'moderate'), ('low', 'low')], max_length=15),
        ),
    ]