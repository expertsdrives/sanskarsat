# Generated by Django 4.2.1 on 2023-05-30 13:21

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0027_alter_introduction_introduction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduction',
            name='introduction',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
