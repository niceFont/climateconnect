# Generated by Django 2.2.13 on 2021-04-20 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('climateconnect_api', '0058_userprofiletranslation_is_manual_translation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofiletranslation',
            name='name_translation',
        ),
    ]
