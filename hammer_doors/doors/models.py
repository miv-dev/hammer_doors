import uuid as uuid
from django.core.exceptions import ValidationError
from django.db import models


# Create your models here
class Branch(models.Model):
    name = models.CharField(max_length=30, verbose_name="Назначение")

    def __str__(self):
        return self.name


class Accessory(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    image = models.ImageField(verbose_name="Фурнитура", upload_to="accessories")


class Film(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    image = models.ImageField(verbose_name="Пленка", upload_to="films")

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=30, verbose_name="Название")
    hex_value = models.CharField(max_length=7, verbose_name="Цвет")

    def __str__(self):
        return self.name


class Panel(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название")
    image = models.ImageField(verbose_name="Фото панели", upload_to="panels")

    def __str__(self):
        return self.name


class Door(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    uuid = models.UUIDField(editable=False, default=uuid.uuid4)
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, verbose_name="Назначение")
    description = models.TextField(max_length=3000  , verbose_name="Описание")
    inside_img = models.OneToOneField(Panel, on_delete=models.CASCADE, verbose_name="Внутреняя панель",
                                      related_name="inside_panel")
    outside_img = models.OneToOneField(Panel, on_delete=models.CASCADE, verbose_name="Внешняя панель",
                                       related_name="outside_panel")

    colors = models.ManyToManyField(Color, verbose_name="Цвета", blank=True)
    accessories = models.ManyToManyField(Accessory, verbose_name="Фурнитура", blank=True)
    films = models.ManyToManyField(Film, verbose_name="Пленки", blank=True)
    tech_info = models.TextField(verbose_name="Техническое описание")
    price = models.IntegerField(verbose_name="Цена")
    popular = models.IntegerField(editable=False, default=0)

    def __str__(self):
        return self.title


class CTA(models.Model):
    title = models.CharField(max_length=30, verbose_name="Название")
    subtitle = models.CharField(max_length=100, verbose_name="Описание")
    door = models.ForeignKey(Door, on_delete=models.CASCADE, verbose_name="Дверь")
    show = models.BooleanField(default=False, verbose_name="Показывать")
