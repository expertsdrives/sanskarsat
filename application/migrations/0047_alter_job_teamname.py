# Generated by Django 4.2.1 on 2023-06-21 13:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0046_ourteam_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='teamName',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, to='application.ourteam'),
        ),
    ]
