
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import ListAPIView, RetrieveAPIView, UpdateAPIView, ListCreateAPIView

from api.serializers import ArticleSerializer
from blog.models import Article


class ArticleApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


