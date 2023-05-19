from django.urls import path
from .views import Login, LogOut, UploadProfile


urlpatterns = [
    path('login', Login.as_view(), name='login'),
    path('logout', LogOut.as_view()),
    path('profile/upload', UploadProfile.as_view()),
]