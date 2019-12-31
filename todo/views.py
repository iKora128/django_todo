from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import ToDoModel


class TodoList(ListView):
    template_name = "list.html"
    model = ToDoModel

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = ToDoModel


