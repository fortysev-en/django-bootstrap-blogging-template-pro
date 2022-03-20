from django import views
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

app_name = 'blogs'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.blogHomepage, name='blog-homepage'),
    path('froala_editor/',include('froala_editor.urls')),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('api/', include('blogs.urls_api'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()