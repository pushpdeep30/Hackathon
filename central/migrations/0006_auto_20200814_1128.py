# Generated by Django 3.0.5 on 2020-08-14 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0005_auto_20200814_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital_records',
            name='available',
            field=models.CharField(default='[0,0,0]', max_length=20),
        ),
        migrations.AlterField(
            model_name='hospital_records',
            name='bed_capacity',
            field=models.CharField(default='[0,0,0]', max_length=20),
        ),
    ]