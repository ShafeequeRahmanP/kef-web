# Generated by Django 3.0.8 on 2020-08-04 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200803_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='additional_info',
            field=models.TextField(default='enter additional information here...'),
        ),
    ]
