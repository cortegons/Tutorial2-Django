from typing import Any
from django.shortcuts import render
# from django.http import HttpResponse
from django.views.generic import TemplateView
# Create your views here.

#def homePageView(request):
#    return HttpResponse('Hello World')

class homePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "About us - Online Store",
            "subtitle": "About us",
            "description": "This is an about page...",
            "author": "Developed by: Camilo Ortegon",
        })
        
        return context