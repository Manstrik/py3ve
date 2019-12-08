from django.db import models

# Create your models here.

# Под моделью мы будем понимать описание таблицы в базе данных в виде класса на языке python
# для этого необходимо унаследовать класс Model модуля models

class Frame(models.Model):
    # индекс - первичный уникальный ключ, по сути "номер" окошка
    # будет создан автоматически
    window_height = models.IntegerField()  # просто создаём "табличку" в базе данных с полем названия переменной
