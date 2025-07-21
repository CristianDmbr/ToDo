from django.shortcuts import render, redirect
from .models import Tasks
from .forms import TaskCreationForm
from django.shortcuts import get_object_or_404

def createTask(request):
    alreadyExistingDatabase = Tasks.objects.all()
    if request.method == 'POST':
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            form.save
        else:
            context = {
                'form' : form,
                'tasks' : alreadyExistingDatabase
            }
            return render(request, 'createTask.html',context)
    
    form = TaskCreationForm()
    context = {
        'form' : form,
        'tasks' : alreadyExistingDatabase
    }
    return render(request, 'createTask.html', context)

def deleteTask(request, task_id):
    task = get_object_or_404(Tasks, id = task_id)
    task.delete()
    return redirect('Main page')

def makeChange(request, task_id):

    task = get_object_or_404(Tasks, id = task_id)

    if request.method == 'POST':

        form = TaskCreationForm(request.POST, instance = task)
        # Binds the form to the already existing object task so instead of creating a new one it will edit current task
        
        if form.is_valid():
            form.save()
            return redirect('Main page URL')
            # Redirects to the already existing main page URL defined as <name = 'Main page URL'>
    else:
    # If the request was not POST, it means the user is opening the edit page not submitting
        form = TaskCreationForm(instance = task)
        # Creates a pre filled form using task's current data which will be displayed once the GET function is activated
    
    # The form is coming from the form object above
    context = {'form': form, 'task': task}
    return render(request, 'editTask.html', context)