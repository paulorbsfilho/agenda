# Generated by Django 2.1.4 on 2018-12-08 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20181208_1640'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='info_field',
            name='name',
        ),
        migrations.AddField(
            model_name='info_field',
            name='types_of_fields',
            field=models.CharField(choices=[('email', 'E-mail'), ('phone', 'Telefone'), ('cell', 'Celular')], default='cell', max_length=5),
            preserve_default=False,
        ),
    ]