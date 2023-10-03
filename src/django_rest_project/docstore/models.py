import os

from django.db import models


class DocCategory(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    is_public = models.BooleanField(verbose_name='Публичный', default=False)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.name}'


class DocFile(models.Model):
    file = models.FileField(upload_to='files/')
    categories = models.ManyToManyField(DocCategory)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.file.name}'


class DocChat(models.Model):
    name = models.CharField(verbose_name='Название', max_length=255)
    slug = models.CharField(verbose_name='Внешний ключ', max_length=255)
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)

    def __str__(self):
        return f'{self.id}: {self.slug}({self.name})'


class DocRequest(models.Model):
    created_at = models.DateTimeField(verbose_name='Создано', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Обновлено', auto_now=True)
    category = models.ForeignKey(DocCategory, on_delete=models.PROTECT)
    related_chat = models.ForeignKey(DocChat, on_delete=models.PROTECT)
    request_str = models.CharField(verbose_name='Запрос', max_length=1000)

    def __str__(self):
        return f'{self.id}: chat - {self.related_chat.name}'
