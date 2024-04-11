from django.contrib import admin
from .models import PopularColor, UserColors


@admin.register(PopularColor)
class PopularColorAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'hue',
        'is_active'
    ]


@admin.register(UserColors)
class UserColorAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'hue',
        'sat',
        'lightness',
    ]
    list_filter = [
        'user'
    ]
    search_fields = [
        'user__username',
        'user__first_name',
        'user__last_name',
    ]
