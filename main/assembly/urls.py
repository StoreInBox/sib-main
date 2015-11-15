from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from . import views
from products import views as products_views


urlpatterns = patterns(
    '',
    url(r'^(?P<category_pk>[\d]+)/(?P<category_slug>[-\w]+)/$', views.ProductListView.as_view(), name='product-list'),
    url(r'^product/(?P<pk>[\d]+)/(?P<slug>[-\w]+)/$', products_views.ProductDetailView.as_view(), name='product-detail'),
    url(r'^$', views.HomeView.as_view(), name='home'),
)

# demo pages:
if settings.DEBUG:
    urlpatterns += patterns(
        '',
        url(r'^demo/cart/$', TemplateView.as_view(template_name='demo/_cart.html'), name='demo-cart'),
    )
