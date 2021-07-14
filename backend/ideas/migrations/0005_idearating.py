# Generated by Django 2.2.18 on 2021-05-06 04:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ideas', '0004_idea_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='IdeaRating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.PositiveSmallIntegerField(default=100, help_text='Rating for each idea by users', verbose_name='Rating')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='Time when rating was given to the idea', verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='Time when user updated their rating for an idea', verbose_name='Updated at')),
                ('idea', models.ForeignKey(help_text='Points to idea table', on_delete=django.db.models.deletion.CASCADE, related_name='rating_idea', to='ideas.Idea', verbose_name='Idea')),
                ('user', models.ForeignKey(help_text='Points to user who rated the idea', on_delete=django.db.models.deletion.CASCADE, related_name='user_rated', to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Idea rating',
                'verbose_name_plural': 'Idea ratings',
            },
        ),
    ]
