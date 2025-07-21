from django import forms
from .models import Tasks

class TaskCreationForm(forms.ModelForm):
    class Meta:
        model = Tasks
        fields = ('task','dueDate','description','progressStatus','importanceRating')