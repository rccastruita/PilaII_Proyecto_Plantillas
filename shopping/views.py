from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, TemplateView
from django.views.generic.base import ContextMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django.shortcuts import render, redirect

from . import models as my_models
from .models import CartItem

from django.db.models import F, Sum, DecimalField

from comments.forms import CommentModelForm
from .forms import CartItemModelForm

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

class ProductCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'shopping.add_product'

    model = my_models.Product
    fields = '__all__'
    template_name = 'shopping/product_create.html'
    success_url = reverse_lazy('product_list')

class ProductUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'shopping.change_product'

    model = my_models.Product
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'
    fields = '__all__'
    template_name = 'shopping/product_update.html'
    success_url = reverse_lazy('product_list')

class ProductDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'shopping.delete_product'

    model = my_models.Product
    pk_url_kwarg = 'product_pk'
    context_object_name = 'product'
    template_name = 'shopping/product_delete.html'
    success_url = reverse_lazy('product_list')

class SoonPageView(TemplateView):
    template_name = 'soon.html'

class CartListView(ListView):
    model = CartItem
    template_name = 'shopping/cart_list.html'
    context_object_name = 'cart'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['subtotal'] = self.get_queryset().aggregate(total_price=Sum(F('count')*F('presentation__price'), output_field=DecimalField()))
        return data

    def get_queryset(self):
        return CartItem.objects.filter(user=self.request.user)
        #return cart.annotate(total_price=F('count') * F('presentation__price'))

class CartDeleteView(DeleteView):
    model = CartItem

    context_object_name = 'cart_item'
    template_name = 'shopping/cart_delete.html'
    success_url = reverse_lazy('cart_list')

class CartCreateView(CreateView):
    model = CartItem
    fields = [
        'presentation',
        'count',
    ]
    template_name = 'shopping/cart_create.html'
    success_url = reverse_lazy('product_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@login_required
def cart_submit(request):
    if request.method == 'POST':
        form = CartItemModelForm(request.POST)
        if form.is_valid():
            try:
                existing_item = CartItem.objects.get(
                    user=request.user, 
                    presentation=request.POST.get('presentation', '')
                )
                existing_item.count = request.POST.get('count', 0)
                existing_item.save()

            except CartItem.DoesNotExist:
                new_item = CartItem(
                    user = request.user,
                    presentation = form.cleaned_data['presentation'],
                    count = form.cleaned_data['count'],
                )
                new_item.save()
                
            return redirect('cart_list')

    else:
        return redirect('product_list')