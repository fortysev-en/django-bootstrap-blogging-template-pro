from django.urls import path

from .views_api import LoginView, SignupView

urlpatterns = [
    path('login/', LoginView),
    path('signup/', SignupView)
]