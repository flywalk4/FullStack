from django.db import models

class Main(models.Model):
    title = models.CharField('Название', max_length=50, default='Название по умолчанию')
    full_text = models.TextField('Текст', blank="True")
    photo = models.ImageField(upload_to="static/photos", blank="True")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'

class Demand(models.Model):
    title = models.CharField('Название', max_length=50, default='Название по умолчанию')
    full_text = models.TextField('Текст', blank="True")
    photo = models.ImageField(upload_to="static/photos", blank="True")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Востребованность'
        verbose_name_plural = 'Востребованность'

class Area(models.Model):
    title = models.CharField('Название', max_length=50, default='Название по умолчанию')
    full_text = models.TextField('Текст', blank="True")
    photo = models.ImageField(upload_to="static/photos", blank="True")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'География'
        verbose_name_plural = 'География'

class Skills(models.Model):
    title = models.CharField('Название', max_length=50, default='Название по умолчанию')
    full_text = models.TextField('Текст', blank="True")
    photo = models.ImageField(upload_to="static/photos", blank="True")
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Навыки'
        verbose_name_plural = 'Навыки'