from django.urls import path
from . import views

urlpatterns = [
	path('', views.news_home_view, name = 'news_home_view'),
]