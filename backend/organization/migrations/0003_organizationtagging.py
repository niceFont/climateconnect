# Generated by Django 2.2.11 on 2020-04-07 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_organizationtags'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganizationTagging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when organization tag was created', verbose_name='Created At')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when organization tag was updated', verbose_name='Updated At')),
                ('organization', models.ForeignKey(help_text='Points to an organization', on_delete=django.db.models.deletion.CASCADE, related_name='tag_organization', to='organization.Organization', verbose_name='Organization')),
                ('organization_tag', models.ForeignKey(help_text='Points to the tag', on_delete=django.db.models.deletion.CASCADE, related_name='tag_organization', to='organization.OrganizationTags', verbose_name='Organization Tag')),
            ],
            options={
                'verbose_name': 'Organization Tagging',
                'verbose_name_plural': 'Organization Taggings',
            },
        ),
    ]
