# Generated by Django 2.1.7 on 2019-03-22 16:40

from django.db import migrations
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0010_storycategory'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymainpage',
            name='categories',
            field=modelcluster.fields.ParentalManyToManyField(blank=True, to='index.StoryCategory'),
        ),
    ]
