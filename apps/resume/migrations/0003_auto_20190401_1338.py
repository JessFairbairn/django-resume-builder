# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-04-01 13:38
from __future__ import unicode_literals

from django.db import migrations
from django.contrib import auth

from django.conf import settings

def create_default_resume(apps, schema_editor):
    UserModel = apps.get_model('auth','User')
    ResumeModel = apps.get_model('resume','Resume')
    ResumeItems = app.get_model('resume','ResumeItem')

    for person in UserModel.objects.all():
        new_resume = ResumeModel.objects.create(title='Default Resume', user=person)
        

class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_auto_20190401_1136'),
    ]

    operations = [
        migrations.RunPython(create_default_resume)
    ]
