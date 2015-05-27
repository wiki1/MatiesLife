# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('articleStatus', models.CharField(max_length=100)),
                ('date_published', models.DateTimeField(verbose_name=b'date published')),
                ('article_image', models.ImageField(upload_to=b'/home/craig/myWiki_gits/ourSite/static/static_dirs')),
                ('category', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.CharField(max_length=200)),
                ('paragraph', models.TextField()),
                ('articles', models.ForeignKey(to='wikiApp.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity_type', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2015, 5, 26, 10, 8, 19, 295513, tzinfo=utc))),
                ('requestStatus', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('user_type', models.IntegerField(default=0)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('date_of_birth', models.DateTimeField(verbose_name=b'date of birth')),
            ],
        ),
        migrations.AddField(
            model_name='requests',
            name='users',
            field=models.ForeignKey(to='wikiApp.Users'),
        ),
        migrations.AddField(
            model_name='articles',
            name='users',
            field=models.ForeignKey(to='wikiApp.Users'),
        ),
    ]
