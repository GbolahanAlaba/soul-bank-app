# Generated by Django 5.0 on 2024-02-17 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Users', '0014_alter_user_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.IntegerField(blank=True, default='', max_length=50, null=True, unique=True),
        ),
    ]
