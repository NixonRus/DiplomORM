# Generated by Django 5.1.3 on 2024-11-13 18:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='boby',
            new_name='body',
        ),
    ]
