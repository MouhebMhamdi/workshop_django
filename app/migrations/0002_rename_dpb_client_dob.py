# Generated by Django 3.2 on 2022-01-27 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='dpb',
            new_name='dob',
        ),
    ]
