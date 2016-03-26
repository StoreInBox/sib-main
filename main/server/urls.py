from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
admin.autodiscover()


urlpatterns = patterns(
    '',
    # Custom applications
    url(r'', include('main.assembly.urls')),
    url(r'', include('export.urls')),
    url(r'', include('cart.urls')),
    url(r'^orders/', include('orders.urls')),
    # Django applications
    url(r'^admin/', include(admin.site.urls)),
)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
