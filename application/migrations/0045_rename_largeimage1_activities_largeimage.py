# Generated by Django 4.2.1 on 2023-06-15 08:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0044_activities_largeimage1_activities_smallimage1_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activities',
            old_name='largeImage1',
            new_name='largeImage',
        ),
    ]
