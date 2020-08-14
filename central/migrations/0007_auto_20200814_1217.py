# Generated by Django 3.0.5 on 2020-08-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0006_auto_20200814_1128'),
    ]

    operations = [
        migrations.AddField(
            model_name='records',
            name='symptoms',
            field=models.CharField(default='[]', max_length=100),
        ),
        migrations.AlterField(
            model_name='hospital_records',
            name='country',
            field=models.CharField(default='India', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital_records',
            name='region',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='records',
            name='medical_history',
            field=models.CharField(default='[]', max_length=100),
        ),
    ]