# Generated by Django 5.0.1 on 2024-02-11 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_attendence', '0012_tsa_sclass'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tsa',
            name='period',
            field=models.CharField(max_length=10),
        ),
    ]
