from urllib import request
from .views import *
from django.urls import path

urlpatterns = [
    path('', InfopageView.as_view(), name='info'),
    path('news/', NewsView.as_view(), name='news'),
    path('projects/', ProjectsView.as_view(), name='projects'),
    path('news/post/<int:pk>/', NewsDetailView.as_view(), name='newspost_dl'),
    path('projects/post/<int:pk>', ProjectsDetailView.as_view(), name='projectpost_dl'),
]