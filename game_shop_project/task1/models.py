from django.db import models
from .models_pg import Category, Developer



class Buyer(models.Model):
    name = models.CharField(max_length=150, verbose_name="Имя покупателя")
    balance = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Баланс", default=0.00)
    age = models.PositiveIntegerField(verbose_name="Возраст")
    password = models.CharField(max_length=255, verbose_name="Пароль", null=True)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название игры")
    cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    size = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Размер файла")
    description = models.TextField(verbose_name="Описание")
    age_limited = models.BooleanField(default=False, verbose_name="Ограничение 18+")
    buyers = models.ManyToManyField(Buyer, related_name="games", verbose_name="Обладатели")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="games", verbose_name="Категория")
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name="games", verbose_name="Разработчик")

    def __str__(self):
        return self.title


