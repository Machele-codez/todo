# Generated by Django 2.2.7 on 2020-04-10 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0010_auto_20200408_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('', 'status'), ('critical', 'critical'), ('high', 'high'), ('moderate', 'moderate'), ('low', 'low')], default='', max_length=15),
            preserve_default=False,
        ),
    ]