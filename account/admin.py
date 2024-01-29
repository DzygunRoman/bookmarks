from django.contrib import admin
from .models import Profile


@admin.register(Profile)# Регистрирую модель Profile на сайте администрирования
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    raw_id_fields = ['user']



