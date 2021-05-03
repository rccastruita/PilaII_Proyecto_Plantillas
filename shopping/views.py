from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import PermissionRequiredMixin

from . import models as my_models
from comments.forms import CommentModelForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ProductListView(ListView):
    model = my_models.Product
    template_name = 'shopping/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView, ContextMixin):
    model = my_models.Product
    template_name = 'shopping/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_pk'

    # Form for posting comments
    extra_context = {'comment_form': CommentModelForm()}

class ProductCreateView(CreateView):
    model = my_models.Product
    fields = '__all__'
    template_name = 'shopping/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(UpdateView):
    model = my_models.Product
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'
    fields = '__all__'
    template_name = 'shopping/product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(DeleteView):
    model = my_models.Product
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'
    template_name = 'shopping/product_delete.html'
    success_url = reverse_lazy('product_list')

class SoonPageView(TemplateView):
    template_name = 'soon.html'