# Generated by Django 5.0.1 on 2024-02-08 13:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='date',
        ),
    ]
