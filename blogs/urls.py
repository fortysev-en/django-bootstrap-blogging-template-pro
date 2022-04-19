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
    path('', views.homepage, name='homepage'),
    path('cookieAcceptance/', views.cookie_acceptance, name='cookie-acceptance'),
    path('froala_editor/',include('froala_editor.urls')),
    path('login/', views.login, name='login'),
    path('myProfile/', views.my_profile, name='my-profile'),
    path('deleteProPic/', views.delete_profile_pic, name='delete-profile-pic'),
    path('signup/', views.signup, name='signup'),
    path('addBlog/', views.add_blog, name='add-blog'),
    path('allBlogs/', views.all_blogs, name='all-blogs'),
    path('blogDetail/<slug>', views.blog_detail, name='blog-detail'),
    path('myBlogs/', views.my_blogs, name='my-blogs'),
    path('blogDelete/<id>', views.blog_delete, name='blog-delete'),
    path('blogUpdate/<int:pk>', views.blog_update, name='blog-update'),
    path('sendForReview/<int:pk>', views.send_for_review, name='send-for-review'),
    path('previewBlog/<int:pk>', views.preview_blog, name='preview-blog'),
    path('logout-view/', views.logout_view, name='logout-view'),
    path('api/', include('blogs.urls_api')),
    path('search/', views.search, name='search-page'),
    path('deleteComment/<id>', views.comment_delete, name='delete-comment'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('privacyPolicy/', views.privacy_policy, name='privacy-policy'),
    path('donatePage/', views.donate, name='donate'),
    path('adminView/', include('blogs.urls_admin')),
    path('userProfile/<str:username>', views.user_profile, name='user-profile'),
    path('subscribe/', views.subscribe, name='subscribe')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()