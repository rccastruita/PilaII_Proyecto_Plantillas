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
    model = MyModels.Producto
    template_name = 'products.html'
    context_object_name = 'productos'

class ProductDetailView(DetailView):
    model = MyModels.Producto
    template_name = 'product_detail.html'
    context_object_name = 'producto'

class ContactListView(ListView):
    model = MyModels.Sucursal
    template_name = 'contact.html'
    context_object_name = 'sucursales'

class ContactCreateView(CreateView):
    model = MyModels.Sucursal
    template_name = 'contact_create.html'
    fields = '__all__'
    success_url = reverse_lazy('contact')

class ContactUpdateView(UpdateView):
    model = MyModels.Sucursal
    template_name = 'contact_update.html'
    fields = '__all__'
    success_url = reverse_lazy('contact')

class ContactDeleteView(DeleteView):
    model = MyModels.Sucursal
    template_name = 'contact_delete.html'
    context_object_name = 'sucursal'
    success_url = reverse_lazy('contact')

class SoonPageView(TemplateView):
    template_name = 'soon.html'