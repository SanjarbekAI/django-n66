from django.contrib import admin

from products.models import Products


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'quantity']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['name']
    ordering = ['-id']
    # date_hierarchy = ['created_at',]

