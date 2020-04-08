# Generated by Django 2.2.7 on 2020-04-06 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['date_created']},
        ),
        migrations.AddField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='text',
            field=models.CharField(max_length=30, unique=True),
        ),
    ]
