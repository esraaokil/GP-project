# Generated by Django 4.0.5 on 2022-06-28 00:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0003_chronic_diseases_doctor_patient_state_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='city_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='state', to='data.state'),
        ),
    ]
