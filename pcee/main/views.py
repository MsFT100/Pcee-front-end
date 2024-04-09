from django.shortcuts import render
from django.views.generic import TemplateView, View

class Index(TemplateView):
    template_name = 'main/index.html'

