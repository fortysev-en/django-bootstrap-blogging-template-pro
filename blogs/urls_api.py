from django.urls import path

from .views_api import *

urlpatterns = [
    path('login/', LoginView),
    path('signup/', SignupView),
    path('comment/', PostComments),
    path('deleteComment/', DeleteComments)
]