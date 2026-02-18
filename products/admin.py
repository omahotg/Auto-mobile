from django.contrib import admin
from .models import Category, Vehicle 

class CarAdmin(admin.ModelAdmin):
    list_display = ('name','make','year','created_at','short_description')
    list_editable = ('make','year','short_description')
    list_filter = ('name', 'category')
    search_fields = ['name', 'make', 'short_description']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'created', 'updated')
    

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vehicle, CarAdmin)