from django.urls import path

from api.views import ArticleApiView, ArticleDetailApiView, ArticleUpdateApiView

urlpatterns = [
    path('', ArticleApiView.as_view()),
    path('<int:pk>', ArticleDetailApiView.as_view()),
    path('update/<int:pk>', ArticleUpdateApiView.as_view()),

]
