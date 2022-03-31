from django.urls import path
from .views_admin import *

urlpatterns = [
    path('admin-panel/', admin_panel, name='admin-panel'),
    path('reviewBlog/', review_blog, name='review-blog'),
    path('userManage/', user_manage, name='user-manage'),
    path('publish-blog/<int:pk>', publish_blog, name='publish-blog'),
    
    path('activateUser/<int:pk>', activate_user, name='activate-user'),
    path('disableUser/<int:pk>', disable_user, name='disable-user'),
    path('changeUserPwd/<int:pk>', change_pwd, name='change-user-pwd'),
    path('deleteUser/<int:pk>', delete_user, name='delete-user'),
    path('resendVerification/<int:pk>', delete_user, name='resend-verification')

]