# Generated by Django 2.1.4 on 2018-12-11 17:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0014_auto_20181211_1641'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='photo',
        ),
    ]
