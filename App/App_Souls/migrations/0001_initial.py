# Generated by Django 5.0 on 2024-01-04 14:58

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Soul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('phone_number', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('address', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('status', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('sector', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('gender', models.BooleanField(default=True)),
                ('age_range', models.CharField(blank=True, default='', max_length=50, null=True)),
                ('description', models.TextField(blank=True, default='', max_length=50, null=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('won_by', models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
