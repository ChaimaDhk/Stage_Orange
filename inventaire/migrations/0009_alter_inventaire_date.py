# Generated by Django 4.2.3 on 2023-09-03 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventaire', '0008_alter_incident_application_alter_incident_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventaire',
            name='Date',
            field=models.CharField(max_length=100),
        ),
    ]
