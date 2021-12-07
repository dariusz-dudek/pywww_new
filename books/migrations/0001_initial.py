# Generated by Django 4.0 on 2021-12-07 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('available', models.BooleanField(default=False)),
                ('publication_year', models.IntegerField()),
                ('author', models.CharField(max_length=255)),
            ],
        ),
    ]
