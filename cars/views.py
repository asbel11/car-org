from django.shortcuts import render
from django.views.generic import UpdateView,ListView,TemplateView,CreateView,DetailView,DeleteView
from .models import Cars
from django.urls import reverse_lazy


class CarsUpdateView(UpdateView):
    model = Cars
    template_name = "post_edit.html"
    fields = ["title", "body","image"]
class HomePageView(ListView):
    model = Cars
    template_name = "home.html"

class AboutPageView(TemplateView):
    template_name = "about.html"

class CarsPageView(TemplateView):
    template_name = "cars.html"

class ShopPageView(TemplateView):
    template_name = "shop.html"

class CarsCreateView(CreateView):
    model = Cars
    template_name = "post_new.html"
    fields = ["title", "author", "body","image",]
class CarsDetailView(DetailView):
    model = Cars
    template_name = "post_detail.html"

class CarsDeleteView(DeleteView):
    model = Cars
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")


