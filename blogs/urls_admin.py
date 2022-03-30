from django.urls import path
from .views_admin import *

urlpatterns = [
    path('admin-panel/', admin_panel, name='admin-panel'),
    path('reviewBlog/', review_blog, name='review-blog'),
    path('userManage/', user_manage, name='user-manage'),
    path('publish-blog/<int:pk>', publish_blog, name='publish-blog')
]