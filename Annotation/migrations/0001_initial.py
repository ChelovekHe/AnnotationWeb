# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=255)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.Dataset')),
            ],
        ),
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='LabeledImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.Image')),
                ('label', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.Label')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('dataset', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.Dataset')),
            ],
        ),
        migrations.AddField(
            model_name='label',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Annotation.Task'),
        ),
    ]
