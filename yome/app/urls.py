from django.urls import path
from .views import acc, login, signup

urlpatterns = [
    path("signup/", signup),
    path("login/", login),
    path("acc/", acc)
]
