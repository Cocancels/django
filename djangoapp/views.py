import imp
from django.shortcuts import render, redirect
from django.http import HttpResponse, response, Http404, HttpResponseRedirect
from .models import Question
from .form import QuestionForm


def index(request):
    try:
        question_list = Question.objects.all()
        context = {
            'questions': question_list,
        }
    except:
        raise Http404("Question does not exist")
    return render(request, 'djangoapp/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
        context = {
            'question': question,
        }
    except Question.DoesNotExist:
        raise Http404("Cette question n'existe pas")
    return render(request, 'djangoapp/detail.html', context)


def create(request):
    if request.method == "POST":

        form = QuestionForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                return redirect('/app/')
            except:
                pass
    else:
        form = QuestionForm()
    context = {
        'form': form,
    }
    return render(request, 'djangoapp/create.html', context)


def edit(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Cette question n'existe pas")

    form = QuestionForm(instance=question)

    if request.method == "POST":
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            try:
                form.save()
                return redirect('/app/')
            except:
                pass
    context = {
        'form': form,
        'question': question,
    }
    return render(request, 'djangoapp/edit.html', context)


def delete(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Cette question n'existe pas")
    question.delete()

    context = {
        'question': question,
    }
    return render(request, 'djangoapp/delete.html', context)
