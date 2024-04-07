from django.contrib import admin
from .models import City


# Register your models here.
@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = ('name',)
