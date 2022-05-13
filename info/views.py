from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import *

class NewsView(ListView):
    model = News
    template_name = 'news.html'

class ProjectsView(ListView):
    model = Projects
    template_name = 'projects.html'

class NewsDetailView(DetailView):
    model = News
    template_name = 'newspost_dl.html'

class ProjectsDetailView(DetailView):
    model = Projects
    template_name = 'projectpost_dl.html'

class InfopageView(ListView):
    model = Achievments
    template_name = 'infopage.html'