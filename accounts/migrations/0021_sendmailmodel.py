# Generated by Django 3.0.3 on 2020-04-01 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0020_nehasimmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SendMailModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=100)),
                ('message', models.CharField(max_length=300)),
            ],
        ),
    ]