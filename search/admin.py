from django.contrib import admin
from .models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'lat_long')
    search_fields = ('name', 'location', 'items')

admin.site.register(Restaurant, RestaurantAdmin)
