# Generated by Django 2.1.4 on 2018-12-09 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0007_auto_20181209_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='photo',
            field=models.ImageField(default='', height_field=40, max_length=200, upload_to='uploads/', width_field=40),
            preserve_default=False,
        ),
    ]
