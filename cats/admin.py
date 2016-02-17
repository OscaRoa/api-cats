from django.contrib import admin
from .models import (
    Cat,
    Breed
)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name',)
        }),
    )

    list_display = ('id', 'name')


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'breed', 'age', 'photo', 'owner')
        }),
    )

    list_display = ('id', 'name', 'breed', 'owner')
