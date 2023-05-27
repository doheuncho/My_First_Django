from django.urls import path
from .views import Main, UploadFeed, UpdateFeed, DeleteFeed, Profile, UploadReply, ToggleBookmark


urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('update', UpdateFeed.as_view()),
    path('delete', DeleteFeed.as_view()),
    path('reply', UploadReply.as_view()),
    path('bookmark', ToggleBookmark.as_view()),
    path('profile', Profile.as_view()),
    path('main', Main.as_view())
]