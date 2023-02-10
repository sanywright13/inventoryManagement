from django.shortcuts import render
from .models import Question
# Create your views here.
from django.http import HttpResponse
def index(request):
    question=Question.objects.order_by('pub_date')
    output=[q for q in question]
    return render(request,'polls/index.html',{
        'output' : output
    })
def detail(request,question_id):
    #get the question of question_id
    question=Question.objects.get(pk=question_id)
    print(question.id)
    try:
        return render(request,'polls/detail.html',{
            'question':question
        })
    except Question.DoesNotExist:
        raise Http404("Question does not exist")

    return HttpResponse(f'you are looking to question {question_id}')
def results(request,question_id):
    return  HttpResponse(f'this is results of auestion ID :{question_id}')
def vote(request,question_id):
    return HttpResponse(f' numbers of vote for question ID :{question_id}')