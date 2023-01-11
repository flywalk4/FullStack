from django.db import models

class Content(models.Model):
    title = models.CharField('Название', max_length=50, default='Название по умолчанию')
    full_text = models.TextField('Текст')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
