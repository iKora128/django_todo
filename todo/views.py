from django.shortcuts import render
from django.views.generic import ListView

class TodoList(ListView):
    template_name = "list.html"


