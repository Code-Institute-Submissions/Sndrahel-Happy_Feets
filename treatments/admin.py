from django.contrib import admin
from .models import Package, Categories


class PackageAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'description',
        'price',
        'image',
    )

    ordering = ('sku',)


class CategoriesAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Package, PackageAdmin)
admin.site.register(Categories, CategoriesAdmin)
