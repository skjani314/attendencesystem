# Generated by Django 5.0.1 on 2024-02-05 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_attendence', '0005_att'),
    ]

    operations = [
        migrations.AlterField(
            model_name='att',
            name='sub_attended',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='att',
            name='sub_total',
            field=models.IntegerField(),
        ),
    ]