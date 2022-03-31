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
    path('myProfile/', views.my_profile, name='my-profile'),
    path('signup/', views.signup, name='signup'),
    path('addBlog/', views.add_blog, name='add-blog'),
    path('blogDetail/<slug>', views.blog_detail, name='blog-detail'),
    path('myBlogs/', views.my_blogs, name='my-blogs'),
    path('blogDelete/<id>', views.blog_delete, name='blog-delete'),
    path('blogUpdate/<int:pk>', views.blog_update, name='blog-update'),
    path('logout-view/', views.logout_view, name='logout-view'),
    path('api/', include('blogs.urls_api')),
    path('search/', views.search, name='search-page'),
    path('deleteComment/<id>', views.comment_delete, name='delete-comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('adminView/', include('blogs.urls_admin')),
    path('userProfile/<id>', views.user_profile, name='user-profile')    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()