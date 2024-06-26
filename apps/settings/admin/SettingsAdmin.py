from django.contrib import admin

__all__ = ['SettingsAdmin']


class SettingsAdmin(admin.ModelAdmin):
    list_display = ('key', 'value', 'data_type')
    list_filter = ('data_type',)
    search_fields = ('key', 'value')
    ordering = ('key', 'data_type')
    fie = (None, {'fields': ('key', 'value', 'data_type')})
    readonly_fields = ('created_at', 'updated_at', 'deleted_at')
