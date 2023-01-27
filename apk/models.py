from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=50)
    op1 = models.CharField(max_length=50)
    op2 = models.CharField(max_length=50)
    op3 = models.CharField(max_length=50)
    op4 = models.CharField(max_length=50)

    def __str__(self):
        return self.question