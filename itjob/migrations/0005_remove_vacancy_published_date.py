# Generated by Django 3.0.8 on 2020-12-20 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('itjob', '0004_auto_20201220_2040'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vacancy',
            name='published_date',
        ),
    ]
