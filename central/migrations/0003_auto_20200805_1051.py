# Generated by Django 3.0.5 on 2020-08-05 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0002_auto_20200805_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='records',
            name='medical_history',
            field=models.CharField(default='[0,0,0,0,0,0,0]', max_length=50),
        ),
    ]