from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200) # CharField class requires max_length
    pub_Date = models.DateTimeField('date published') # First argument to a Field is a human-readable name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # Defines each instance of class Choice as necessarily related to an instance of class Question
    # on_delete=CASCADE signifies that all objects that have references to an instance of this class should be deleted if the class instance is deleted
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # Optional argument
