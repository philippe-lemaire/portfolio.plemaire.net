# Generated by Django 3.2.9 on 2021-11-06 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_rename_caterogy_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pub_time',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
