from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import ToDoModel


class TodoList(ListView):
    template_name = "list.html"
    model = ToDoModel

class TodoDetail(DetailView):
    template_name = "detail.html"
    model = ToDoModel

class TodoCreate(CreateView):
    template_name = "create.html"
    model = ToDoModel
    fields = ("title", "memo", "priority", "duedate")


