# Generated by Django 4.2.8 on 2024-06-24 16:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_delete_post'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-fixed', '-create'], 'verbose_name': 'Статья Блога', 'verbose_name_plural': 'Статьи Блога'},
        ),
    ]
