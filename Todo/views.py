from django.shortcuts import render, redirect
from .models import Todo
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,'index.html')
@csrf_exempt
def view(request):
    todos = Todo.objects.all()
    return render(request, 'view.html', {'todos': todos})

@csrf_exempt
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        completed = request.POST.get('completed','no')
        todo = Todo(name=name, description=description, completed=completed)
        todo.save()
        messages.success(request, 'Todo added successfully')
        return redirect('view')
    return render(request,'add.html')
@csrf_exempt
def edit(request,pk):
    todo = Todo.objects.get(pk=pk)
    if request.method == 'POST':
        todo.name = request.POST.get('name')
        todo.description = request.POST.get('description')
        todo.completed = request.POST.get('completed', False)
        todo.save()
        messages.success(request, 'Todo updated successfully')
        return redirect('view')
    return render(request,'edit.html', {'todo': todo})
@csrf_exempt
def delete(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.delete()
    messages.success(request, 'Todo deleted successfully')
    return redirect('view')
    



