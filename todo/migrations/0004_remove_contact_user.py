# Generated by Django 3.1.14 on 2023-01-05 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='user',
        ),
    ]
