# Generated by Django 5.1.1 on 2024-10-30 20:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Users', '0002_remove_role_name_role_admin_role_member_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='role',
            old_name='sector_lead',
            new_name='sec_lead',
        ),
    ]
