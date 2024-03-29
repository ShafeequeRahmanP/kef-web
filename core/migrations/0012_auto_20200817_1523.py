# Generated by Django 3.0.8 on 2020-08-17 09:53

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_auto_20200817_0001'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='from_email',
            new_name='email',
        ),
        migrations.AddField(
            model_name='message',
            name='contact_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
