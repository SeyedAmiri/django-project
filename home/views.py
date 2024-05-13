# from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from .forms import TodoCreateForm

# def hello(request):
#     return HttpResponse("Hello User...")


def home(request):
    all = Todo.objects.all()
    return render(request, 'home.html', context={'all': all})


def hello(request):
    person = {'name': 'admin'}
    return render(request, 'hello.html', context=person)


def detail(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    return render(request, 'detail.html', context={'todo': todo})


def delete(request, todo_id):
    Todo.objects.get(id=todo_id).delete()
    messages.success(request, 'todo deleted successfully!', extra_tags='success')
    return redirect('home')


def create(request):
    form = TodoCreateForm()
    return render(request, 'create.html', context={'form': form})