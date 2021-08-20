# Create your views here.
from django.contrib.auth.models import User
from rest_framework.generics import ListCreateAPIView, \
    RetrieveUpdateAPIView, ListAPIView

from api.permissions import IsSuperUserOrReadOnly, IsAuthorOrReadOnly
from api.serializers import ArticleSerializer, UserSerializer
from blog.models import Article


class ArticleApiView(ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ArticleDetailApiView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = (IsAuthorOrReadOnly,)


class ArticleUpdateApiView(RetrieveUpdateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class UserApiView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperUserOrReadOnly,)


class UserDetailApiView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
