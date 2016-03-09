from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static

from . import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
   url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)