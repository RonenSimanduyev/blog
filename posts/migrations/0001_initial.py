# Generated by Django 4.0.2 on 2022-04-12 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('imageUrl', models.CharField(max_length=400)),
                ('body', models.TextField()),
                ('created', models.DateField(auto_now_add=True)),
            ],
        ),
    ]