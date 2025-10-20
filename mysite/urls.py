from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from places.views import index

urlpatterns = (
    [
        path("admin/", admin.site.urls),  # Админка Django
        path("ckeditor/", include("ckeditor_uploader.urls")),  # Маршруты для CKEditor
        path("", index),  # Нулевой эндпоинт
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
