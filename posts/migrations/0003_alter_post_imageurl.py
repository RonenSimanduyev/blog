# Generated by Django 4.0.2 on 2022-06-21 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_alter_post_imageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imageUrl',
            field=models.CharField(blank=True, max_length=400),
        ),
    ]
