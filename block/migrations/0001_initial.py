# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-03-25 11:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bizname', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Neighbourhood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hood_name', models.CharField(max_length=50)),
                ('hood_location', models.CharField(max_length=50)),
                ('occupants', models.IntegerField(blank=True, null=True)),
                ('admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_image', models.ImageField(default='default.jpeg', upload_to='')),
                ('me', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('myhood', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Neighbourhood')),
            ],
        ),
        migrations.AddField(
            model_name='business',
            name='bizhood',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='block.Neighbourhood'),
        ),
        migrations.AddField(
            model_name='business',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
