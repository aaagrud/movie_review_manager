# Generated by Django 5.0.6 on 2024-05-28 04:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_director'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movieinfo',
            old_name='description',
            new_name='summary',
        ),
    ]
