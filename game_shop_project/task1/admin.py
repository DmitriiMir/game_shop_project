from django.contrib import admin
from .models import Buyer

@admin.register(Buyer)
class BuyerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'balance', 'age', 'password')

    search_fields = ('name', 'password')

    list_filter = ('age',)

    list_editable = ('balance', 'age')

    fields = ('name', 'balance', 'age', 'password')

    readonly_fields = ('id',)

    ordering = ('-id',)
