from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'category'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=150)
    website = models.URLField(blank=True, null=True)
    founded_at = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'developer'
        verbose_name = 'Разработчик'
        verbose_name_plural = 'Разработчики'

    def __str__(self):
        return self.name
