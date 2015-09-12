from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^products/$', views.ProductListView.as_view(), name='products'),
)
