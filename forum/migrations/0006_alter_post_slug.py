# Generated by Django 4.2.16 on 2024-10-16 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0005_alter_reply_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(blank=True, max_length=200, unique=True),
        ),
    ]
