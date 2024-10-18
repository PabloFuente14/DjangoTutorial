from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    #when the user submits the form the server recieves the POT request and processes here
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #retrieves the choice selected by the user
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn`t select a choice",
        },)
    else:
        selected_choice.votes =F("votes") + 1 #incrementing directly in database
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results",args = (question.id,)))#redirects user the results page


from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from .models import Question,Choice
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F

from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


def vote(request, question_id):
    #when the user submits the form the server recieves the POT request and processes here
    question = get_object_or_404(Question, pk = question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"]) #retrieves the choice selected by the user
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            "question": question,
            "error_message": "You didn`t select a choice",
        },)
    else:
        selected_choice.votes =F("votes") + 1 #incrementing directly in database
        selected_choice.save()
    return HttpResponseRedirect(reverse("polls:results",args = (question.id,)))#redirects user the results page


