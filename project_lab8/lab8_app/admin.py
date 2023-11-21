from django.contrib import admin
from .models import Provider, Material, Supply

@admin.register(Provider)
class ProviderAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_person', 'phone', 'account')

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')

@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('date', 'provider', 'material', 'days', 'amount')