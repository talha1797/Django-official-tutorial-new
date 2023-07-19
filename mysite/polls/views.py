from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question, Choice
from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.urls import reverse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:15]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)

def add_choice(request, question_id):
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/add_choice.html", {"question": question})

def adding_user_choice(request, question_id):
    submit_user_choice= request.POST['add_choice']
    question = get_object_or_404(Question, pk=question_id)

    new_choice= Choice(
        question=question,
        choice_text=submit_user_choice
    )
    new_choice.save()
    return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))


def add_question(request):
    return render(request, "polls/add_question.html")


def adding_user_question(request):
    submit_user_question= request.POST['adding_user_question']
    new_question = Question(question_text=submit_user_question,  pub_date=timezone.now())
    new_question.save()
    context = {"new_question": new_question}
    return HttpResponseRedirect(reverse("polls:index"))


def edit_question(request,question_id):
     question = get_object_or_404(Question, pk=question_id)
     return render(request, "polls/edit_question.html", {"question": question})


def user_edit_question(request,question_id):
    question= get_object_or_404(Question, pk=question_id)
    submit_user_question= request.POST['user_edit_question']
    question.question_text=submit_user_question,
    question.pub_date=timezone.now()
    question.save()
    context = {"question":question}
    return HttpResponseRedirect(reverse("polls:detail", args=(question.id,)))
