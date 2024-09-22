# Generated by Django 5.1.1 on 2024-09-22 16:04

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='prediction',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='location',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/img/prediction/'),
        ),
        migrations.AddField(
            model_name='prediction',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='update_date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='prediction',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='prediction',
            name='title',
            field=models.CharField(max_length=160),
        ),
    ]