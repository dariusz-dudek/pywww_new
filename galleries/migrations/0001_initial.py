# Generated by Django 3.2.8 on 2022-01-04 19:30

import common.models
from django.db import migrations, models
import django.db.models.deletion
import galleries.models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.models.CheckAgeMixin),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.TextField(max_length=255)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('short_description', models.CharField(blank=True, max_length=300, null=True)),
                ('image', sorl.thumbnail.fields.ImageField(upload_to=galleries.models.upload_to)),
                ('source', models.CharField(blank=True, max_length=512, null=True)),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='photos', to='galleries.gallery')),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model, common.models.CheckAgeMixin),
        ),
    ]
