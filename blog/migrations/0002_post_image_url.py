# Generated by Django 4.0.3 on 2023-03-28 14:39

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=blog.models.upload_to),
        ),
    ]
