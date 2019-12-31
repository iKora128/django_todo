
from django.urls import path, include
from .views import todo

urlpatterns = [
    path("list/", TodoList.as_view()),
]