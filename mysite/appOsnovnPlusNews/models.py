from django.db import models

# таблица с постами
class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Имя компании', max_length=50)
    textPost = models.TextField('Описание компании')
    date = models.DateTimeField('Дата публикации')
    chairts = models.TextField('Характеристики')
    image = models.TextField('Изображения')
# краткий формат вывода(не уверен)
    def __str__(self):
        return str(self.name)