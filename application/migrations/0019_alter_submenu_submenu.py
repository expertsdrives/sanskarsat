# Generated by Django 4.2.1 on 2023-05-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0018_remove_submenu_submenuname_submenu_menu_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submenu',
            name='subMenu',
            field=models.CharField(blank=True, default='', max_length=256),
        ),
    ]