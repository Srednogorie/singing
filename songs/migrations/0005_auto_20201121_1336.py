# Generated by Django 3.1.3 on 2020-11-21 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0004_customuser_user_avatar'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_avatar',
            new_name='avatar',
        ),
    ]
