# Generated by Django 4.0.6 on 2023-01-16 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_user_login1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Login1',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
