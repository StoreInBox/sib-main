# coding: utf-8
import json

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View

from products import models as products_models


class HomeView(View):

    def get(self, request):
        return render(request, 'home/home.html')


class ProductListView(ListView):
    paginate_by = 12
    allow_empty = True

    def get(self, request, *args, **kwargs):
        self.category = self._get_category()
        if request.is_ajax() and 'count' in request.GET:
            return HttpResponse(
                json.dumps(self.get_queryset().count()),
                content_type='application/json',
            )
        return super(ProductListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        return self.category.get_products().filter(is_active=True)

    def get_template_names(self):
        template = super(ProductListView, self).get_template_names()[0]
        if self.request.is_ajax():
            return template[:-5] + '_ajax.html'
        return template

    def get_paginate_by(self, queryset):
        """
        Paginate by specified value in querystring, or use default class property value.
        """
        key = self.__class__.__name__ + '_rows'
        if 'paginate_by' in self.request.GET:
            try:
                self.paginate_by = max(int(self.request.GET.get('paginate_by', self.paginate_by)), 5)
                self.request.session[key] = self.paginate_by
            except ValueError:
                pass
        else:
            self.paginate_by = self.request.session.get(key, self.paginate_by)
        return self.paginate_by

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['count'] = self.get_queryset().count()
        context['category'] = self.category
        return context

    def _get_category(self):
        return get_object_or_404(
            products_models.Category, pk=self.kwargs['category_pk'], slug=self.kwargs['category_slug'])
