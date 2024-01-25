from django.urls import path
from .views import (BlogList, AboutPageView, AddPostView)

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('', BlogList.as_view(), name='home'),
    path('add_post/', AddPostView.as_view(), name="add_post"),
]