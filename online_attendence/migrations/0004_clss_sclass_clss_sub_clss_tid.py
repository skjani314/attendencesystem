# Generated by Django 5.0.1 on 2024-02-04 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_attendence', '0003_remove_clss_sclass_remove_clss_sub_remove_clss_tid'),
    ]

    operations = [
        migrations.AddField(
            model_name='clss',
            name='sclass',
            field=models.CharField(default='cse4', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clss',
            name='sub',
            field=models.CharField(default='dsp', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='clss',
            name='tid',
            field=models.CharField(default='t2001', max_length=10),
            preserve_default=False,
        ),
    ]
