# Generated by Django 2.2.5 on 2019-12-22 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veterinary', '0016_auto_20191222_0344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='illnessappointment',
            name='date_start',
            field=models.DateField(auto_now_add=True),
        ),
    ]
