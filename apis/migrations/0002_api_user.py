# Generated by Django 2.2 on 2020-02-26 05:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='api',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apis', to=settings.AUTH_USER_MODEL),
        ),
    ]
