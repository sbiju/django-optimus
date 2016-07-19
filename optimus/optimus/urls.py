from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from profiles.views import HomePageView


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    # url(r'^quiz/', include('quiz.urls')),
    url(r'', include('profiles.urls')),
    url(r'^$', HomePageView.as_view(), name='home'),
    # url(r'^grappelli/', include('grappelli.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
