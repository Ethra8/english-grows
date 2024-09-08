from django.contrib import admin
from .models import IndivService, IndividualType


class IndivServiceAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'price',
        'image',
    )

    ordering = ('sku',)

class IndividualTypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(IndivService)
admin.site.register(IndividualType)



