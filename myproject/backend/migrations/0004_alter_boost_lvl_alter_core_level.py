# Generated by Django 4.2.7 on 2023-11-02 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_core_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boost',
            name='lvl',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='core',
            name='level',
            field=models.IntegerField(default=1),
        ),
    ]
