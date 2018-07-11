from django.shortcuts import render
from easycart import BaseCart, BaseItem

from mainapp.models import Bike


class Cart(BaseCart):

    def get_queryset(self, pks):
        return Bike.objects.filter(pk__in=pks)


BaseItem.PRICE_ATTR = "cost"
