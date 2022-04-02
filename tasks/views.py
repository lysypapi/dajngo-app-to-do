from django.shortcuts import redirect, render , get_object_or_404
from .models import Task
from .forms import TaskForm

# Create your views here.

def index(request):
    tasks = Task.objects.all()
    form = TaskForm(request.POST or None)
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'tasks':tasks,
        'form':form
    }
    return render(request,'tasks/home.html',context)

def update(request,id):
    task = get_object_or_404(Task,id=id)
    form = TaskForm(instance=task)
    if request.method == 'POST':
        form = TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
        return redirect('/')
    context = {
        'form':form
    }
    return render(request,'tasks/update_task.html',context)

def delete(request,id):
    task = get_object_or_404(Task,id=id)
    if request.method == "POST":
        task.delete()
        return redirect('/')
    return render(request,'tasks/delete_task.html',{'task':task})

