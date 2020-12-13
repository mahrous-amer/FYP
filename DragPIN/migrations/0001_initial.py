# Generated by Django 3.1.4 on 2020-12-13 05:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('DragID', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('PIN', models.CharField(max_length=4, validators=[django.core.validators.RegexValidator(code='invalid_Pin', message='Pin must be 4 numerics', regex='[0-9][0-9][0-9][0-9]')])),
            ],
        ),
    ]