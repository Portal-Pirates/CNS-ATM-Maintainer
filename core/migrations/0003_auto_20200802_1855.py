# Generated by Django 3.0.8 on 2020-08-02 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200802_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='working_location',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
