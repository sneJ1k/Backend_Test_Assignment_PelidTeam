from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Place(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название")
    description_short = models.TextField(verbose_name="Короткое описание", blank=True)
    description_long = RichTextUploadingField(
        verbose_name="Длинное описание", blank=True
    )
    lng = models.FloatField(verbose_name="Долгота")
    lat = models.FloatField(verbose_name="Широта")

    def __str__(self):
        return self.title


class Image(models.Model):
    place = models.ForeignKey(Place, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="places/", verbose_name="Изображение")
    order = models.PositiveIntegerField(default=0, verbose_name="Порядок")

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"Изображение для {self.place.title}"
