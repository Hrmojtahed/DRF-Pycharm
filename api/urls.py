from django.urls import path, include

from api.views import ArticleApiView, ArticleDetailApiView, ArticleUpdateApiView, UserApiView, UserDetailApiView

urlpatterns = [
    path(
        "api-auth/", include("rest_framework.urls")
    ),
    path('', ArticleApiView.as_view()),
    path('<int:pk>', ArticleDetailApiView.as_view()),
    path('update/<int:pk>', ArticleUpdateApiView.as_view()),
    path('users', UserApiView.as_view()),
    path('users/<int:pk>', UserDetailApiView.as_view()),

]
