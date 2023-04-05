from django.contrib import admin
from django.contrib.auth.models import Group
from rest_framework.authtoken.models import TokenProxy

from recipes.models import Favorite, Cart
from .models import Subscriptions, User


admin.site.unregister(TokenProxy)
admin.site.unregister(Group)


class FavoriteInline(admin.TabularInline):
    model = Favorite
    fields = ('user', 'recipe',)


class CartInline(admin.TabularInline):
    model = Cart
    fields = ('user', 'recipe',)


class SubscribeInline(admin.TabularInline):
    model = Subscriptions
    fk_name = 'user'
    fields = ('user', 'author',)


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    inlines = (FavoriteInline, CartInline, SubscribeInline,)
    list_display = ('pk', 'username', 'email', 'first_name', 'last_name')
    list_filter = ('username', 'email')
    search_fields = ('username', 'email')
    empty_value_display = '-пусто-'


@admin.register(Subscriptions)
class SubscribeAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'author')
    list_editable = ('user', 'author')
    empty_value_display = '-пусто-'
