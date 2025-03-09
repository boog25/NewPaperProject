from django.urls import path
from .views import news_list, news_detail, news_search, news_create, news_edit, news_delete

urlpatterns = [
    path('', news_list, name='news_list'),
    path('<int:pk>/', news_detail, name='news_detail'),
    path('search/', news_search, name='news_search'),
    path('create/', news_create, name='news_create'),
    path('<int:pk>/edit/', news_edit, name='news_edit'),
    path('<int:pk>/delete/', news_delete, name='news_delete'),
]