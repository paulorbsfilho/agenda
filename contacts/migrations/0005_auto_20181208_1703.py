# Generated by Django 2.1.4 on 2018-12-08 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20181208_1701'),
    ]

    operations = [
        migrations.RenameField(
            model_name='info_field',
            old_name='types_of_fields',
            new_name='type_of_field',
        ),
    ]