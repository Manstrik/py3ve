from django.db import models
from django.core.validators import int_list_validator
from django.core.validators import RegexValidator


# Create your models here.

# Под моделью мы будем понимать описание таблицы в базе данных в виде класса на языке python
# для этого необходимо унаследовать класс Model модуля models

class Frame(models.Model):
    # индекс - первичный уникальный ключ, по сути "номер" окошка
    # будет создан автоматически
    window_height = models.IntegerField(default=50)
    # просто создаём "табличку" в базе данных с полем названия переменной
    window_width = models.IntegerField(default=50)
    scheme = models.CharField(
        validators=[
            RegexValidator('\{(\d+:\[\d+(,\d+)*\],)*\}')],
        default='{}',
        max_length=256)
