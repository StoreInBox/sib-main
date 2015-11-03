# coding: utf-8
from django.shortcuts import render
from django.views.generic import View

from filters import models as filters_models
from products import views as products_views


class HomeView(View):

    def get(self, request):
        return render(request, 'home/home.html')


class ProductListView(products_views.ProductListView):
    paginate_by = 12
    allow_empty = True

    def get(self, request, *args, **kwargs):
        self.category = self._get_category()
        self.filters = filters_models.FilterMixin.get_category_filters(self.category)
        return super(ProductListView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = super(ProductListView, self).get_queryset()
        # filtering
        for f in self.filters:
            queryset = f.filter(queryset, self.request)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['filters'] = {f.get_template_name(): f for f in self.filters}
        return context
