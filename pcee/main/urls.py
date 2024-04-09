
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as  main_views;

urlpatterns = [
    path('', main_views.Index.as_view(), name="index"),
]
