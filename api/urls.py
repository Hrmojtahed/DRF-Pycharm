
from django.contrib import admin
from django.urls import path,include

from api.views import ArticleApiView

urlpatterns = [
    path('',ArticleApiView.as_view() ),


]