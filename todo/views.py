from django.shortcuts import render, redirect, Http404
from todo.models import  Tasks
from todo.forms import TaskForm

# Create your views here.

def index(request):
    tasks = Tasks.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
        return redirect('todo:home')
    return render(request, 'index.html',context={'form':form, 'tasks':tasks})


def update_task(request, pk):
    try:
        task = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        raise Http404
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                task.completed = True if request.POST.get('completed') == 'on' else False
                task.title  =   request.POST.get('title')
                task.save(update_fields=('title', 'completed'))
            except AttributeError:
                raise Http404

        return redirect('todo:home')

    return render(request, 'update.html', {'form': form})


def delete_task(request, pk):
    try:
        task = Tasks.objects.get(id=pk)
        if request.method == 'POST':
            task.delete()
            return redirect('todo:home')
    except Tasks.DoesNotExist:
        raise Http404
    return render(request, 'delete.html', {})

