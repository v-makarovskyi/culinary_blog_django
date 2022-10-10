from enum import auto
from django.db import models

class Photo(models.Model):
    """ класс модели фото галереи изображений  """
    name = models.CharField(max_length=250)
    image = models.ImageField(upload_to='gallery/')
    captions = models.TextField(max_length=255, blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name


class Gallery(models.Model):
    """ класс модели галереи изображений """
    name = models.CharField(max_length=250)
    images = models.ManyToManyField(Photo)
    captions = models.TextField(max_length=255 ,blank=True)
    create_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name





