from django.contrib import admin

from pizza.models import (
    PizzaMenuItem,
    PizzaSize,
    PizzaIngredient,
    PizzaOrder,
)

from forms import PizzaOrderAdminForm

class PizzaSizeModel(admin.ModelAdmin):
    list_display = ['size', 'full_name', ]

admin.site.register(PizzaSize, PizzaSizeModel)


class PizzaMenuItemModel(admin.ModelAdmin):
    def ingredients_list(self, obj):
        return ', '.join(i.name for i in obj.ingredients.all())
    ingredients_list.short_description = 'Ingredients'

    list_display = ('name', 'ingredients_list')

admin.site.register(PizzaMenuItem, PizzaMenuItemModel)


class PizzaIngredientModel(admin.ModelAdmin):
    list_display = ('name', )

admin.site.register(PizzaIngredient, PizzaIngredientModel)


class PizzaOrderModel(admin.ModelAdmin):
    list_display = ('kind', 'size', 'delivered' )
    form = PizzaOrderAdminForm

    def has_add_permission(self, request):
        return False

admin.site.register(PizzaOrder, PizzaOrderModel)