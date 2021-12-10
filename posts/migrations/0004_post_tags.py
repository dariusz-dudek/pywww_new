# Generated by Django 4.0 on 2021-12-10 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_slug'),
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(related_name='posts', to='tags.Tag'),
        ),
    ]