# Generated by Django 2.2 on 2020-05-04 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0002_api_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiFake',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=128)),
            ],
        ),
    ]
