# Generated by Django 4.2.1 on 2023-05-26 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SLogo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sanskarsetlogo', models.ImageField(max_length=256, upload_to='')),
            ],
        ),
    ]
