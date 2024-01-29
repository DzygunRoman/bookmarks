from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls')),
]

if settings.DEBUG: # используется только в разработке функция вспомогательная функция  static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Панель администрирования" #меняем заголовок админ-панели на свой
admin.site.index_title = "Профиль" #меняем подзаголовок приложения в админ-панели