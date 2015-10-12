# coding: utf-8
from __future__ import unicode_literals

from django.utils.translation import ugettext

from filters import models as filters_models


class PriceFilter(filters_models.NumericProductFieldFilterMixin):

    def get_field(self):
        return 'price'

    @classmethod
    def is_default(cls):
        return True

    @classmethod
    def get_default_creation_kwargs(cls):
        return {'name': ugettext('Price'), 'priority': 100}

    def get_template_name(self):
        return 'price'


class BrandFilter(filters_models.ChoicesProductFieldFilterMixin):

    def get_field(self):
        return 'brand'

    @classmethod
    def is_default(cls):
        return True

    @classmethod
    def get_default_creation_kwargs(cls):
        return {'name': ugettext('BrandFilter'), 'priority': 10}

    def get_template_name(self):
        return 'brand'
