from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from home import views, user_views

from . import settings

urlpatterns = [
                  url(r'^$', views.index),
                  url(r'^lessons/$', views.lessons),
                  url(r'^lessons/(?P<lesson_number>\w+)/$', views.lessons),
                  url(r'^quiz/(?P<quizID>\w+)/$', views.quizes),
                  url(r'^reference/$', views.reference),

                  url(r'^forum/$', views.forum),
                  url(r'^forum/post/$', views.post),
                  url(r'^forum/post/(?P<post>\w+)/$', views.post),
                  url(r'^forum/reply/(?P<post>\w+)/$', views.add_reply),

                  url(r'^faq/$', views.faq),
                  url(r'^dashboard/$', views.dashboard),
                  url(r'^language_specific/$', views.language_specific),
                  url(r'^language_specific/(?P<title>\w+)/$', views.language_specific),
                  url(r'^about_us/$', views.about_us),

                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

                  url(r'^account/', include('django.contrib.auth.urls')),
                  url(r'^login/$', user_views.login_view, name='login'),
                  url(r'^register/$', user_views.register_view, name='register'),
                  url(r'^logout/$', user_views.logout_view, name='logout'),
              ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
