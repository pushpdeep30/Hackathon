# Generated by Django 3.0.5 on 2020-08-11 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('central', '0003_auto_20200805_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hospital_records',
            old_name='subd',
            new_name='region',
        ),
        migrations.AddField(
            model_name='hospital_records',
            name='country',
            field=models.CharField(default='', max_length=20),
        ),
    ]
