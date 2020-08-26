# Generated by Django 3.0.8 on 2020-08-03 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200802_2042'),
    ]

    operations = [
        migrations.DeleteModel(
            name='RexItem',
        ),
        migrations.AddField(
            model_name='item',
            name='additional_image_1',
            field=models.ImageField(default='pictures/a.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='additional_image_2',
            field=models.ImageField(default='pictures/b.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='additional_image_3',
            field=models.ImageField(default='pictures/c.jpg', upload_to=''),
        ),
        migrations.AddField(
            model_name='item',
            name='additional_info',
            field=models.TextField(default='wwdDAJWNDajwh'),
        ),
    ]