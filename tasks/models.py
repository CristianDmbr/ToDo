from django.db import models
from django.utils import timezone

class Tasks(models.Model):

    class ProgressStatus(models.TextChoices):
        NOTSTARTER = 'not_started','Not Started'
        INPROGRESS = 'in_progress', 'In Progress'
        FINISHED = 'finished', 'Finished'
    
    class ImportanceRating(models.TextChoices):
        OPTIONAL = 'optional', 'Optional'
        MEDIUM = 'medium', 'Medium'
        IMPORTANT = 'important', 'Important'

    task = models.CharField( max_length=20 )
    dateTimeCreated = models.DateTimeField( default = timezone.now)
    dueDate = models.DateField( null = True, blank = True)
    description = models.TextField( blank = True )

    progressStatus = models.CharField(
        max_length = 20,
        choices = ProgressStatus.choices,
        default = ProgressStatus.NOTSTARTER
        )
    
    importanceRating = models.CharField(
        max_length = 20,
        choices = ImportanceRating.choices,
        default = ImportanceRating.OPTIONAL
    )

    class Meta:
        ordering = ['-dateTimeCreated']

    def __str__(self):
        return self.task