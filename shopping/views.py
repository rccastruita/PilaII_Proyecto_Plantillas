from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from django.urls import reverse_lazy
from django.views.generic.base import ContextMixin

from . import models as MyModels
from comments.forms import CommentForm

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ProductListView(ListView):
    model = MyModels.Product
    template_name = 'shopping/product_list.html'
    context_object_name = 'products'

class ProductDetailView(DetailView, ContextMixin):
    model = MyModels.Product
    template_name = 'shopping/product_detail.html'
    context_object_name = 'product'
    pk_url_kwarg = 'product_pk'

    extra_context = {'comment_form': CommentForm()}

class SoonPageView(TemplateView):
    template_name = 'soon.html'