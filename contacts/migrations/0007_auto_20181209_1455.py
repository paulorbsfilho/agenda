# Generated by Django 2.1.4 on 2018-12-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20181208_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
