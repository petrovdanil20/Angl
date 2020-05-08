import re

from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from pip._vendor import requests

from AcademicWriting.forms import EssayForm, EssayCheckForm, AuthUserForm
from AcademicWriting.models import Articles


class LoginView(LoginView):
    template_name = 'login_page.html'
    form_class = AuthUserForm
    success_url = 'profile'
    def get_success_url(self):
        return self.success_url


class Logout(LogoutView):
    next_page = reverse_lazy('articles')


class ArticlesListView(ListView):
    model = Articles
    template_name = 'articles.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Articles
    template_name = 'article_details.html'
    context_object_name = 'article'

def profile(request):
    if (not request.user.is_anonymous):
        context = {
        }
        template = 'profile_page.html'
        return render(request, template, context)
    else:
        return HttpResponseRedirect("login")


def checkEssay(request):
    if request.method == "POST":
        text = request.POST.get("text")
        wordsNumber = countWords(text)
        mistakes = findMistakes(text)
        percentage = int((len(mistakes)/wordsNumber*100))
        paragraphs = finParagraphs(text)
        context = {
            "text": text.splitlines(),
            "words": wordsNumber,
            "paragraphs": paragraphs,
                #len(text.splitlines()),
            "spwords": '*TODO*',
            "mistakes": ', '.join(mistakes),
            "percentage": percentage
        }
        template = 'check_essay_result.html'
        return render(request, template, context)
    else:
        essayForm = EssayCheckForm()
        context = {
            "form": essayForm
        }
        template = 'check_essay.html'
        return render(request, template, context)


def home(request):
    context = {
    }
    template = 'base.html'
    return render(request, template, context)

def deleteExtraSpaces(text):
    return re.sub(r'\s+', ' ', text)


def countWords(text):
    return len(text.split())


def countParagraphs(text):
    return len(text.split(sep='\n'))


def findMistakes(text):
    try:
        request = requests.get(
            'https://speller.yandex.net/services/spellservice.json/checkText',
            params={'text': text, 'options': 518}
        )
        return [mis['word'] for mis in request.json()]
    except:
        return ['Connection error']

def finParagraphs(text):
    a = 0
    for elements in text.splitlines():
        if elements != "":
            a = a + 1
    return a
