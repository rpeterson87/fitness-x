# Generated by Django 4.1.2 on 2022-10-10 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_exercises'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercises',
            old_name='exercise',
            new_name='workout',
        ),
    ]