# Generated by Django 3.0.3 on 2020-04-01 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='Month',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
