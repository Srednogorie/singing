# Generated by Django 3.1.3 on 2020-11-21 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0005_auto_20201121_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='band',
            field=models.CharField(default='Lili Ivanova', max_length=200),
            preserve_default=False,
        ),
    ]