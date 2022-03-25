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
    path('', views.Homepage, name='homepage'),
    path('froala_editor/',include('froala_editor.urls')),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('add-blog/', views.add_blog, name='add-blog'),
    path('blog-detail/<slug>', views.blog_detail, name='blog-detail'),
    path('my-blogs/', views.my_blogs, name='my-blogs'),
    path('blog-delete/<id>', views.blog_delete, name='blog-delete'),
    path('blog-update/<int:pk>', views.blog_update, name='blog-update'),
    path('logout-view/', views.logout_view, name='logout-view'),
    path('api/', include('blogs.urls_api')),
    path('search/', views.search, name='search-page'),
    path('delete-comment/<id>', views.comment_delete, name='delete-comment')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()