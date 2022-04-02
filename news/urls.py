from django.urls import path
from .views import PostList, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>/', PostDetailView.as_view(), name='news_detail'),
    path('create/', PostCreateView.as_view(), name='news_create'),
    path('create/<int:pk>', PostUpdateView.as_view(), name='news_update'),
    path('delete/<int:pk>', PostDeleteView.as_view(), name='news_delete'),
]