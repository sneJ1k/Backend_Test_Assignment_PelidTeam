from django.contrib import admin
from .models import Place, Image


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ("image", "order")


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    list_display = ("title", "lat", "lng")
    search_fields = ("title",)
    fields = ("title", "description_short", "description_long", "lat", "lng")
