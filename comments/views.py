from django.shortcuts import render, redirect
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin, AccessMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy

from .forms import CommentModelForm
from .models import Comment
from shopping.models import Product

# Create your views here.
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, DeleteView):
    """ Delete a selected comment """
    model = Comment
    template_name = 'comments/comment_delete.html'
    context_object_name = 'comment'
    # Argument for the comment pk in the url (<int:comment_pk>)
    pk_url_kwarg = 'comment_pk'

    # Message displayed int the 403 error page
    permission_denied_message = 'No cuentas con los permisos suficientes para borrar comentarios de terceros.'

    def test_func(self): # Condition for allowing access
        return self.get_object().user == self.request.user

    def get_success_url(self): # Redirect to this url after delete
        return reverse_lazy('product_detail', kwargs={'product_pk': self.get_object().product.pk})

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, AccessMixin, UpdateView):
    model = Comment
    template_name = 'comments/comment_update.html'
    context_object_name = 'comment'
    pk_url_kwarg = 'comment_pk'

    # Class of the form to be used
    form_class = CommentModelForm

    permission_denied_message = 'No cuentas con los permisos suficientes para editar comentarios de terceros.'

    def test_func(self):
        return self.get_object().user == self.request.user
    
    def get_success_url(self):
        return reverse('product_detail', kwargs={'product_pk': self.get_object().product.pk})

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentModelForm
    template_name = 'comments/comment_create.html'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.product = Product.objects.get(pk=self.kwargs['product_pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('product_detail', kwargs={'product_pk': self.object.product.pk})

""" Function based CreateView (unused)
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
        context = {'comment_form': form, 'product': product}

    return render(request, 'shopping/product_detail.html', context=context)
"""