# Generated by Django 3.1.3 on 2020-11-21 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0003_auto_20201114_1542'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='user_avatar',
            field=models.ImageField(blank=True, upload_to='profile_pics/'),
        ),
    ]
