from django.apps import AppConfig


class ImagesConfig(AppConfig):
    verbose_name = "Изображение"#название приложения в админ-панели
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'images'
