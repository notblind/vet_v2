# Generated by Django 2.2.5 on 2019-12-21 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0005_auto_20191219_2246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaclientmodel',
            name='age',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
