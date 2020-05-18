# Generated by Django 2.2.11 on 2020-04-14 05:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0009_projecttagging_projecttags'),
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(help_text='Content of the post', verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when post was created', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when post was updated', verbose_name='Updated at')),
                ('is_hidden', models.BooleanField(default=False, help_text='If post has made hidden from public', verbose_name='Is hidden?')),
                ('deleted_at', models.DateTimeField(blank=True, help_text='Time when post was deleted', null=True, verbose_name='Deleted at')),
                ('author_user', models.ForeignKey(blank=True, help_text='Points to a user who wrote the post', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_author', to=settings.AUTH_USER_MODEL, verbose_name='Author')),
                ('deleted_by_user', models.ForeignKey(blank=True, help_text='User who deleted the post', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post_delete', to=settings.AUTH_USER_MODEL, verbose_name='Deleted by user')),
                ('project', models.ForeignKey(help_text='Points to post of the project', on_delete=django.db.models.deletion.PROTECT, related_name='post_project', to='organization.Project', verbose_name='Project')),
            ],
            options={
                'verbose_name': 'Posts',
            },
        ),
    ]
