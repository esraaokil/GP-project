# Generated by Django 4.0.5 on 2022-06-28 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_alter_state_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='state',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='id'),
        ),
    ]
