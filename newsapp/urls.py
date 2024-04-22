from django.urls import path
from . import views
from .views import get_headlines

urlpatterns = [
    path('', views.index, name='index'),
    path('categories/', views.categories, name='categories'),
    path('headlines/<str:category>/', get_headlines, name='get_headlines'),
]
