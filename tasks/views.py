from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskCreationForm
from django.shortcuts import get_object_or_404

def createTask(request):
    alreadyExistingTasks = Tasks.objects.all()
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid:
            form.save()
        else:
            context = {
                'form' : form,
                'tasks' : alreadyExistingTasks
                }
            return render(request, 'createTask.html', context)
    
    form = TaskCreationForm()
    context = {
        'form' : form,
        'tasks' : alreadyExistingTasks
        }
    return render(request, 'createTask.html', context)

def delete_task(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    task.delete()
    return redirect('Task creation')