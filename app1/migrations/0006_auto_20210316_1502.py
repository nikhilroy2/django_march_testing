# Generated by Django 3.1.7 on 2021-03-16 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20210316_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crud_create',
            old_name='search',
            new_name='date',
        ),
    ]
