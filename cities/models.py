from django.db import models
from django.urls import reverse


# Create your models here.
class City(models.Model):
    name = models.CharField(max_length=100, unique=True, verbose_name='Назва города')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'
        ordering = ["-pk"]
