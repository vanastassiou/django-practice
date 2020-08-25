from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This is the polls app's index.")

def detail(request, question_id):
    return HttpResponse("This is question %s" % question_id)

def results(request, question_id):
    return HttpResponse("These are the results for question %s" % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s" % question_id)
