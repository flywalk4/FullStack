# Generated by Django 4.1.4 on 2023-01-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Название по умолчанию', max_length=50, verbose_name='Название')),
                ('full_text', models.TextField(verbose_name='Текст')),
                ('photo', models.ImageField(upload_to='uploads/%Y/%m/%d/')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
            ],
            options={
                'verbose_name': 'Главная',
                'verbose_name_plural': 'Параграф',
            },
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
