# Generated by Django 4.2.8 on 2024-06-21 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_vacancy_options_vacancy_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, verbose_name='URL'),
        ),
    ]