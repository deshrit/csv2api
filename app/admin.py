from django.contrib import admin

from .models import Animal


class AnimalAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Animal._meta.get_fields()]
    ordering = ["unique_id"]


admin.site.register(Animal, AnimalAdmin)
