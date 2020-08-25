from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list} # context is a dict mapping template var names to Python objects (key and value must be named the same)
    return render(request, 'polls/index.html', context) # can sub in dict instead of defining a var containing a dict

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raiseHttp404("The requested question does not exist. Sorry about that.")
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    return HttpResponse("These are the results for question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)