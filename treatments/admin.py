from django.contrib import admin
from .models import Package, Category


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Package, PackageAdmin)
admin.site.register(Category, CategoryAdmin)
