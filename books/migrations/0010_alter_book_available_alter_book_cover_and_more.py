# Generated by Django 4.0 on 2021-12-20 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0002_alter_tag_slug'),
        ('books', '0009_borrow'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='available',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.ImageField(null=True, upload_to='books/covers/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(related_name='books', to='tags.Tag'),
        ),
        migrations.DeleteModel(
            name='Borrow',
        ),
    ]