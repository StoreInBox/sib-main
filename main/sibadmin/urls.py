from django.conf.urls import patterns, url

from . import views


urlpatterns = patterns(
    '',
    url(r'^sibadmin/categories/$', views.CategoriesView.as_view(), name='sibadmin-categories'),
)
