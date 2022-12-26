from django.db import models

class Product(models.Model):
    title = models.CharField(verbose_name='Название',max_length=200)
    desc = models.CharField(verbose_name='Описание', max_length=200)
    img = models.ImageField(upload_to='images')