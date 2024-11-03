from django.contrib import admin
from .models import IndivService, IndividualType



admin.site.register(IndivService)
class IndivServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'price',
        'image',
    )

    ordering = ('sku',)


admin.site.register(IndividualType)
class IndividualTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )




