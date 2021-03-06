# Generated by Django 3.1.4 on 2021-04-11 09:37

from django.db import migrations
import taggit_selectize.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('blog', '0006_post_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='tags',
            field=taggit_selectize.managers.TaggableManager(blank=True, help_text='A comma-separated list of tags.', through='tags.TaggedItem', to='tags.Tag', verbose_name='tags'),
        ),
    ]
