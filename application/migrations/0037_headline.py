# Generated by Django 4.2.1 on 2023-06-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0036_topheadertext_tllogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='HeadLine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headLine', models.CharField(max_length=256)),
            ],
        ),
    ]