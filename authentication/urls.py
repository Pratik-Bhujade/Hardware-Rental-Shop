from . import views
from django.conf.urls import url,include
from django.contrib.auth import login, logout
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.SignIn.as_view(), name = 'login'),
    url(r'^logout/$', views.SignOut.as_view(), name = 'logout'),
    url(r'^$', views.home, name='home'),
    url(r'^tools/(?P<type>[0-9]+)$', views.tool, name='tool')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
