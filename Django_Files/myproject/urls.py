from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from home import views, user_views

from . import settings

urlpatterns = [
                  url(r'^$', views.index),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
                  url(r'^account/', include('django.contrib.auth.urls')),
                  url(r'^login/$', user_views.login_view, name='login'),
                  url(r'^register/$', user_views.register_view, name='register'),
                  url(r'^logout/$', user_views.logout_view, name='logout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
