from django.urls import path
from .views import *

urlpatterns = [
    path('list', CreateNewsList.as_view()),
    path('list/<int:pk>', EditNewsList.as_view()),
    path('list_reverse', NewsListReverse.as_view()),   
]
