# Generated by Django 3.2.9 on 2021-11-18 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('folio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='cover_img',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]