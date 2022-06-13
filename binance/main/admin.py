from django.contrib import admin

from .models import Coin, CoinName 


@admin.register(Coin)
class CoinAdmin(admin.ModelAdmin):
	list_display = ('name', 'price', 'market_cap', )
	prepopulated_fields = {'slug': ('name', )}


@admin.register(CoinName)
class CoinNameAdmin(admin.ModelAdmin):
	list_display = ('name', )