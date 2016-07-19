# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import profiles.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MasterProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'abc', max_length=80)),
                ('last_name', models.CharField(default=b'abc', max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to=profiles.models.upload_location, blank=True)),
                ('gender', models.CharField(max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'N', b'Not Disclosed')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='ParticipantProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'abc', max_length=80)),
                ('last_name', models.CharField(default=b'abc', max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('photo', models.ImageField(null=True, upload_to=profiles.models.upload_location, blank=True)),
                ('gender', models.CharField(max_length=2, choices=[(b'M', b'Male'), (b'F', b'Female'), (b'N', b'Not Disclosed')])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
