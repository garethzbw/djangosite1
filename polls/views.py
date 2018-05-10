from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from polls.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('create_date')

    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})

def detail(request, question_id):
    return


def results(request, question_id):
    return


def answer(request, question_id, answer_content):
    return
