from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Catog, Product

@admin.register(Catog)
class CatogAdmin(ImportExportModelAdmin):
    list_display = ['name', 'status', 'created_at']

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ['name', 'vendor', 'catof', 'quantity', 'selling_price', 'status', 'created_at']
