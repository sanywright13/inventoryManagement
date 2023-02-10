from django.db import models

# Create your models here.
class Question(models.Model):
    question_text=models.CharField(max_length=63)
    pub_date=models.DateTimeField()

    '''
    def __str__(self):
        return f' question : {self.question_text} published the : {self.pub_date}'
    '''

class Choice1(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)  
    choice_text=models.CharField(max_length=200,null=0, blank=0,)
    votes=models.IntegerField(default=0)      