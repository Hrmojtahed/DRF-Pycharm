# Create your views here.
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, \
    RetrieveUpdateAPIView

from api.serializers import ArticleSerializer
from blog.models import Article


class ArticleApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailApiView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleUpdateApiView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
