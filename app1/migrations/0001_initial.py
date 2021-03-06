# Generated by Django 3.1.7 on 2021-03-14 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_url', models.TextField()),
                ('hash', models.TextField(unique=True)),
            ],
            options={
                'db_table': 'url_shortener',
            },
        ),
    ]
