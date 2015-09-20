# coding: utf-8
from __future__ import unicode_literals

from django.db import models

from filters import models as filters_models
from products import models as products_models


class BaseFilter(models.Model):
    class Meta:
        abstract = True

    # objects = ProductFilterManager()

    category = models.ForeignKey(products_models.Category, null=True)

    def get_related_products(self):
        return self.category.get_products()


# TODO: Propagate filters to subcategories

class NumericPriceFilter(filters_models.NumericFilterMixin, BaseFilter):

    def _get_min_and_max(self, request):
        selected_max_value = request.GET.get('{}-max'.format(self.get_item_prefix()), self.max_value)
        selected_min_value = request.GET.get('{}-min'.format(self.get_item_prefix()), self.min_value)
        return selected_min_value, selected_max_value

    def filter(self, queryset, request):
        selected_min_value, selected_max_value = self._get_min_and_max(request)
        filter_query = self.get_filter_query('price_uah', selected_min_value, selected_max_value)
        return queryset.filter(filter_query)

    def update(self):
        return super(NumericPriceFilter, self).base_update(field='price_uah')

    def get_queryset(self):
        products = self.get_related_products()
        return products_models.ProductConfiguration.objects.filter(product__in=products)
