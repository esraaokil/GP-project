# Generated by Django 4.0.5 on 2022-07-02 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0009_rename_cities_citiess'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='city_id',
        ),
        migrations.DeleteModel(
            name='citiess',
        ),
    ]