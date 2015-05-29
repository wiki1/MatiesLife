# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('wikiApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_image',
            field=models.ImageField(upload_to=b'/home/hendrik/GIT/ourSite/static/media'),
        ),
        migrations.AlterField(
            model_name='requests',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 5, 29, 9, 59, 52, 7399, tzinfo=utc)),
        ),
    ]
