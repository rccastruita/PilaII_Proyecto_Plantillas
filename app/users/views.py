from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from .models import User
from . import forms as my_forms

class UserCreateView(UserPassesTestMixin, CreateView):
    """User creation view
    UserPassesTestMixin checks the condition returned by test_func()
    If false, redirects to login or sends a 403 error
    """
    form_class = my_forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'

    # Responds with a 403 error instead of redirecting to login
    raise_exception = True
    # 403 error message
    permission_denied_message = 'Necesitas cerrar la sesión actual para crear una nueva cuenta.'
    # Function to check if there is a current user authenticated
    def test_func(self):
        return self.request.user.is_anonymous

class UserUpdateView(LoginRequiredMixin, UpdateView):
    """View for updating the current user info
    LoginRequiredMixin checks that only authenticated users can access the view
    """
    # Redirect to login if user not logged in
    login_url = reverse_lazy('login')

    form_class = my_forms.UserChangeForm
    success_url = reverse_lazy('home')
    template_name = 'users/user_update.html'

    # Get current user data
    def get_object(self, queryset=None):
        return self.request.user