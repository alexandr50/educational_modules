from django.contrib import admin

from bank_card.models import BankCard

@admin.register(BankCard)
class BankCardAdmin(admin.ModelAdmin):
    list_display = ('date',)
    exclude = ('csv',)
