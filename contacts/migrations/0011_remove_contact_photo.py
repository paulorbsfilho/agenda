# Generated by Django 2.1.4 on 2018-12-10 17:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0010_auto_20181210_1239'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='photo',
        ),
    ]