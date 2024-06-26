# Generated by Django 4.2.8 on 2024-06-26 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_blog_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='BannerIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('image', models.ImageField(upload_to='banners/', verbose_name='Изображение')),
                ('published_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
            ],
            options={
                'verbose_name': 'Баннер_Главная',
                'verbose_name_plural': 'Баннеры_Главная',
                'ordering': ['-published_at'],
            },
        ),
    ]
