# Generated by Django 3.1.7 on 2021-03-18 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tag', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=100),
        ),
    ]