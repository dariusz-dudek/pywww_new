# Generated by Django 4.0 on 2021-12-11 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_post_example_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='example_image',
            field=models.ImageField(null=True, upload_to='posts/images/%Y/%m/%d'),
        ),
    ]