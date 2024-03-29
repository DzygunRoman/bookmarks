from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='images_crated', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/', verbose_name='Изображение')
    description = models.TextField(blank=True, verbose_name='Описание')
    created = models.DateField(auto_now_add=True)
    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='images_liked', blank=True)


    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

        verbose_name = "Изображение"  # замена в админ-панели категории блога
        verbose_name_plural = "Изображения"  # множественное число категории

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
