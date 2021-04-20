from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from .forms import CommentForm
from .models import Comment
from shopping.models import Product

# Create your views here.
class CommentDetailView(DetailView):
    model = Comment
    pk_url_kwarg = 'comment_pk'

class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, DeleteView):
    model = Comment
    template_name = 'comments/comment_delete.html'
    context_object_name = 'comment'
    pk_url_kwarg = 'comment_pk'

    permission_denied_message = 'No cuentas con los permisos suficientes para borrar comentarios de terceros.'

    def test_func(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('product_detail', kwargs={'product_pk': self.get_object().product.pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, UpdateView):
    model = Comment
    template_name = 'comments/comment_update.html'
    context_object_name = 'comment'
    pk_url_kwarg = 'comment_pk'

    fields = ['rating', 'body']

    permission_denied_message = 'No cuentas con los permisos suficientes para editar comentarios de terceros.'

    def test_func(self):
        return self.get_object().user == self.request.user
    
    def get_success_url(self):
        return reverse('product_detail', kwargs={'product_pk': self.get_object().product.pk})

@login_required
def comment_create_view(request, product_pk):
    product = Product.objects.get(pk=product_pk)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_comment = Comment(
                user = request.user,
                product = product,
                body = form.cleaned_data['body'],
            )

            new_comment.save()
            return redirect(product)

    else:
        form = CommentForm()
        context = {'form': form, 'product': product}

    return render(request, 'comment_create.html', context=context)