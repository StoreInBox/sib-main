# coding: utf-8
import inspect
import sys

from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.views.generic import View
from django.shortcuts import render, get_object_or_404

from products import models as products_models


class BaseAdminView(View):
    name = NotImplemented
    description = NotImplemented
    icon = NotImplemented
    page_template = NotImplemented

    @classmethod
    def get_url(cls):
        raise NotImplementedError

    @staticmethod
    def get_all_admin_views():
        return [cls for _, cls in inspect.getmembers(sys.modules[__name__], inspect.isclass)
                if issubclass(cls, BaseAdminView) and cls != BaseAdminView]

    def get_context(self, request):
        print self.get_all_admin_views()
        return {
            'name': self.name,
            'description': self.description,
            'all_admin_views': self.get_all_admin_views(),
        }

    def get(self, request):
        return render(request, 'sibadmin/pages/{}'.format(self.page_template), self.get_context(request))


class CategoriesView(BaseAdminView):
    name = 'Categories'
    description = ''
    icon = 'fa-th'
    page_template = 'categories.html'

    @classmethod
    def get_url(cls):
        return reverse('sibadmin-categories')

    def get_context(self, request):
        context = super(CategoriesView, self).get_context(request)
        context['top_categories'] = products_models.Category.get_top_categories()
        return context

    def delete(self, request, category_id):
        get_object_or_404(products_models.Categories, id=category_id).delete()
        return HttpResponse(status=204)
