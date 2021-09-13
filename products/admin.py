from django.contrib import admin

# Register your models here.
from .models import Product, Category

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'category',
        'price',
    )

    ordering = ('title',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
