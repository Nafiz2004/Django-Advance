from django.urls import path
from .views import UserInfoView

app_name = 'teaching_app'

urlpatterns = [
    path('register/',UserInfoView,name='register'),
]
