# Generated by Django 3.1 on 2023-09-27 03:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='accounnt',
            old_name='user_name',
            new_name='username',
        ),
    ]
