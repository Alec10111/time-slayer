# Generated by Django 3.2.14 on 2022-07-19 13:09

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0004_auto_20220719_1300'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Current_Goals',
            new_name='Current_Goal',
        ),
    ]
