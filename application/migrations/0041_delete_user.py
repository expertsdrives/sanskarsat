# Generated by Django 4.2.1 on 2023-06-02 07:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0040_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]