# Generated by Django 2.2.5 on 2019-12-18 23:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0003_animaclientmodel_animalmodel_breedmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='breedmodel',
            name='animal',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='personal.AnimalModel'),
            preserve_default=False,
        ),
    ]
