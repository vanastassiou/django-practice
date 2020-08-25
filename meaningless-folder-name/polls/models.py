import datetime

from django.db import models
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField class requires max_length
    pub_date = models.DateTimeField('date published') # First argument to a Field is a human-readable name

    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.get() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Defines each instance of class Choice as necessarily related to an instance of class Question
    # on_delete=CASCADE signifies that all objects that have references to an instance of this class should be deleted if the class instance is deleted
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # Optional argument

    def __str__(self):
        return self.choice_text