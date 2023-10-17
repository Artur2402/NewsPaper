from django.urls import path
from .views import PostList, PostDetail, Search, PostCreate, PostEdit, PostDelete, ArticleCreate, ArticleEdit, \
    ArticleDelete, subscriptions

urlpatterns = [
    path('news/', PostList.as_view(), name='post_list'),
    path('news/<int:pk>', PostDetail.as_view(), name='post_detail'),
    path('news/search/', Search.as_view(), name='search'),

    path('news/create/', PostCreate.as_view(), name='post_create'),
    path('news/<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('news/<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

    path('news/article/create/', ArticleCreate.as_view(), name='article_create'),
    path('news/article/<int:pk>/edit/', ArticleEdit.as_view(), name='article_edit'),
    path('news/article/<int:pk>/delete/', ArticleDelete.as_view(), name='article_delete'),
    path('news/subscriptions/', subscriptions, name='subscriptions'),

]