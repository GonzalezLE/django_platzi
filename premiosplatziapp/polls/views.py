from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Question, Choice

from django.views.generic import (
    DetailView,
    ListView
)

class IndexView(ListView):
    template_name  = 'polls/index.html'
    context_object_name = 'lastes_question_list'
    
    def get_queryset(self):
        """return the last five publiched question
        """    
        return Question.objects.order_by('-pub_date')[:5]


# def index(request):
#     lastes_question_list = Question.objects.all()

#     return render(request, 'polls/index.html', {
#         'lastes_question_list': lastes_question_list
#     })



class DetailView(DetailView):
    model = Question
    template_name = 'polls/detail.html'
    
    
# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)

#     return render(request, 'polls/detail.html', {
#         'question': question
#     })



class ResultView(DetailView):
    model = Question
    template_name = 'polls/results.html'



# def results(request, question_id):
#     question = get_object_or_404(Question,pk = question_id)

#     return render(request,'polls/results.html',{
#         'question' : question
#     })



# funtion base view
def vote(request, question_id):

    question = get_object_or_404(Question, pk=question_id)

    try:

        selected_choice = question.choice_set.get(pk=request.POST['choice'])

    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        # return HttpResponseRedirect(reverse("polls:results", args=[question.id]))
        return HttpResponseRedirect(
            reverse(
                "polls:results",
                args=(question.id,)
            )
        )
