# Generated by Django 2.2.3 on 2020-06-02 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cers', '0004_auto_20200602_2159'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ['-accepted_at']},
        ),
    ]
