from django.urls import path
from .views import UserModelView,UserLogin

app_name = 'basic_app'

urlpatterns = [
    path('register/',UserModelView,name='register'),
    path('login',UserLogin,name='login'),
]
