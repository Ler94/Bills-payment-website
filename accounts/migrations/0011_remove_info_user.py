# Generated by Django 3.0.3 on 2020-03-30 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_delete_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info',
            name='user',
        ),
    ]
