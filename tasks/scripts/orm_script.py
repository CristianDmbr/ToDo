from tasks.models import Tasks
from django.utils import timezone

def run():
    
    example = Tasks.objects.create(
        task = 'Go down to 75kg',
        dueDate = '2025-09-09',
        description = "Dont forget to maintain caloric deficit.",
        progressStatus = Tasks.ProgressStatus.INPROGRESS,
        importanceRating = Tasks.ImportanceRating.IMPORTANT
    )

    print(f"The newly created Task is : ", {example.task}, " and its due : ", {example.dueDate})