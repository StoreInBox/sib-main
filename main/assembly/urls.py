from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^(?P<category_id>[\d+])/(?P<category_slug>[-\w]+)/$', views.ProductListView.as_view(), name='products'),
    url(r'^$', views.HomeView.as_view(), name='home'),
)
