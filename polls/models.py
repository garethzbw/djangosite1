from django.db import models

# Create your models here.

from django.db import models

class Question(models.Model):
    context = models.CharField(max_length=200)
    create_date = models.DateTimeField()


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.DO_NOTHING)
    content = models.CharField(max_length=100)
    votes = models.IntegerField(default=0)