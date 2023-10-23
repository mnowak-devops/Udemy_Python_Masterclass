from datetime import datetime
from django.shortcuts import render
from django.http import response, HttpResponse
from django.views import View
from django.shortcuts import render

from .models import ArticleModel


# Create your views here.
class Home(View):
    def get(self, request):
        return HttpResponse("Welcome to my blog")
    def post(self, request):
        return HttpResponse("[POST] Welcome to my blog")


class Article(View):
    def get(self, request):
        articles = ArticleModel.objects.all()

        return render(request, "articles.html",{"articles":articles})