from django.urls import path
from .views_admin import *

urlpatterns = [
    path('admin-panel/', admin_panel, name='admin-panel'),
    path('adminMessages/', admin_messages, name='admin-messages'),
    # path('mark-message/<int:pk>', mark_message, name='mark-message'),
    # path('delete-message/<int:pk>', delete_message, name='delete-message'),
    path('markMessage/', mark_msg, name='mark-message'),
    path('deleteMessage/', delete_msg, name='delete-message'),

    path('reviewBlog/', review_blog, name='review-blog'),
    path('userManage/', user_manage, name='user-manage'),
    path('publish-blog/<int:pk>', publish_blog, name='publish-blog'),

    path('activateUser/<int:pk>', activate_user, name='activate-user'),
    path('disableUser/<int:pk>', disable_user, name='disable-user'),
    path('changeUserPwd/<int:pk>', change_pwd, name='change-user-pwd'),
    path('deleteUser/<int:pk>', delete_user, name='delete-user'),
    path('resendVerification/<int:pk>', resend_verification, name='resend-verification')

]