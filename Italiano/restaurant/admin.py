from django.contrib import admin

from . import models

class DishAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'recomended')

admin.site.register(models.Category)
admin.site.register(models.Dish, DishAdmin)
admin.site.register(models.Reservation)
admin.site.register(models.Contact)