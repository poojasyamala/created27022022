from . import views
from django.urls import path
from .views import getAddressDetails, login_user, login_template
urlpatterns = [
    path('POST/getAddressDetails/', getAddressDetails, name = 'address'),
    path('POST/login_user', login_user, name = "login-user"),
    path('GET/login_template', login_template, name = "login_template")
]