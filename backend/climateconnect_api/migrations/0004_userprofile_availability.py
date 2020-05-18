# Generated by Django 2.2.11 on 2020-04-04 16:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('climateconnect_api', '0003_availability'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='availability',
            field=models.ForeignKey(blank=True, help_text="Points to user's availability for a work", null=True, on_delete=django.db.models.deletion.PROTECT, related_name='user_availability', to='climateconnect_api.Availability', verbose_name='Availability'),
        ),
    ]
