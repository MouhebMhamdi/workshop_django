# Generated by Django 3.2 on 2022-02-03 14:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projet',
            name='temps_allocated',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'le temps min doit etre 1 heure')]),
        ),
    ]
