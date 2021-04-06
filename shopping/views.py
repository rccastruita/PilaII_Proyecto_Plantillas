from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy

from . import models as MyModels

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ProductListView(ListView):
    model = MyModels.Product
    template_name = 'products.html'
    context_object_name = 'productos'

class ProductDetailView(DetailView):
    model = MyModels.Product
    template_name = 'product_detail.html'
    context_object_name = 'producto'

class SoonPageView(TemplateView):
    template_name = 'soon.html'