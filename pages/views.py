from typing import Any
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import TemplateView
from django.views import View
from django import forms
from django.shortcuts import render, redirect
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
    
class ContactPageView(TemplateView):
    template_name = "contact.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            "title": "Contact us - Online Store",
            "subtitle": "Contact us",
            "email": "example@mail.com",
            "address": "17 St 8B-10",
            "phonenumber": "1234567890"
        })
        
        return context

class Product:
    products = [
        {"id":"1", "name":"TV", "description":"Best TV", "price": 300},
        {"id":"2", "name":"iPhone", "description":"Best iPhone", "price": 500},
        {"id":"3", "name":"Chromecast", "description":"Best Chromecast", "price": 400},
        {"id":"4", "name":"Glasses", "description":"Best Glasses", "price": 60},
    ]
    
class ProductIndexView(View):
    template_name = "products/index.html"
    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products
        
        return render(request, self.template_name, viewData)
    
class ProductShowView(View):
    template_name = 'products/show.html'
    def get(self, request, id):
        viewData = {}
        try:
            product = Product.products[int(id)-1]
            viewData["subtitle"] = product["name"] + " - Product information"
            viewData["product"] = product
            
            return render(request, self.template_name, viewData)
        
        except (IndexError, ValueError):
            return HttpResponseRedirect(reverse("home"))
    
    
class ProductForm(forms.Form):
    name = forms.CharField(required=True)
    price = forms.FloatField(required=True)
    
    def clean(self):
        price = self.cleaned_data.get("price")
        if price <= 0:
            raise forms.ValidationError("Price can't be less or equal zero")
    
class ProductCreateView(View):
    template_name = "products/create.html"
    created_template_name = "products/created.html"
    
    def get(self, request):
        form = ProductForm()
        viewData = {}
        viewData["title"] = "Create product"
        viewData["form"] = form
        
        return render(request, self.template_name, viewData)
    
    def post(self, request):
        form = ProductForm(request.POST)
        if form.is_valid():
            return render(request, self.created_template_name, {"title": "Product created"})
        else:
            viewData = {}
            viewData["title"] = "Create product"
            viewData["form"] = form
            return render(request, self.template_name, viewData)
        