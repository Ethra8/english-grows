from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):

    readonly_fields = ('user', 'default_full_name', 'default_email',
                        'default_phone_number', 'default_country')

    fields = ('default_full_name', 'default_email',
                        'default_phone_number')

    list_display = ('user', 'default_full_name', 'default_email',
                        'default_phone_number', 'default_country')

    ordering = ('-user',)


admin.site.register(UserProfile)