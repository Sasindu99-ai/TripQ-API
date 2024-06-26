from django.contrib import admin

from ..models import Currency, Setting
from .CurrencyAdmin import CurrencyAdmin
from .SettingsAdmin import SettingsAdmin

admin.site.register(Setting, SettingsAdmin)
admin.site.register(Currency, CurrencyAdmin)
