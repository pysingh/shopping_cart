# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-01 09:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('photo', models.ImageField(default='default.jpg', upload_to=b'')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('charge_id', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Cat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('image', models.ImageField(default='default.jpg', upload_to=b'')),
                ('p_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Category')),
            ],
        ),
        migrations.RenameField(
            model_name='item',
            old_name='item_id',
            new_name='id',
        ),
        migrations.AddField(
            model_name='item',
            name='item_id1',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='item',
            name='photo',
            field=models.ImageField(default='default.jpg', upload_to=b''),
        ),
    ]