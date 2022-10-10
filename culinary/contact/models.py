from django.db import models

class ContactModel(models.Model):
    """ Класс модели обратной связи """
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.URLField(blank=True, null=True)
    message = models.TextField(max_length=5000)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name} - {self.email}'


class ContactLink(models.Model):
    """  Класс модели контактов """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class About(models.Model):
    """ Класс модели страницы О нас """
    name = models.CharField(max_length=200, default='')
    text = models.TextField()
    mini_text = models.TextField()

    def get_first_image(self):
        item = self.about_images.first()
        return item.image.url

    def get_images(self):
        return self.about_images.order_by('id')[1:]


class ImageAbout(models.Model):
    """ Класс модели изображений страницы О нас """
    image = models.FileField(upload_to='about/')
    page = models.ForeignKey(About, related_name='about_images', on_delete=models.CASCADE)
    alt = models.CharField(max_length=100)


class Social(models.Model):
    """ Класс модели социальных сетей страницы О нас """
    icon = models.FileField(upload_to='icons/')
    name = models.CharField(max_length=200)
    link = models.URLField()