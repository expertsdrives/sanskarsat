# Generated by Django 4.2.1 on 2023-05-30 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0021_alter_submenu_submenu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='submenu',
            name='subMenu',
        ),
        migrations.AddField(
            model_name='submenu',
            name='submenu',
            field=models.TextField(blank=True, default=''),
        ),
    ]
