# Generated by Django 4.2.1 on 2023-05-26 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appOsnovnPlusNews', '0002_posts_chairts_posts_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='posts',
            name='chairts',
        ),
        migrations.RemoveField(
            model_name='posts',
            name='image',
        ),
    ]
