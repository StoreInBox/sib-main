from django.conf.urls import patterns, url, include

from . import views
import export


urlpatterns = patterns(
    '',
    url(r'^(?P<category_pk>[\d+])/(?P<category_slug>[-\w]+)/$', views.ProductListView.as_view(), name='products'),
    url(r'^$', views.HomeView.as_view(), name='home'),
)
