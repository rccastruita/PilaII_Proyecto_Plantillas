from django.urls import path, include
from django.contrib.auth.views import LoginView

from . import views as my_views

urlpatterns = [
    path('signup/', my_views.UserCreateView.as_view(), name='signup'),
    path('edit/', my_views.UserUpdateView.as_view(), name='user_update'),
    path('login/', LoginView.as_view(redirect_authenticated_user=True)),
    path('', include('django.contrib.auth.urls')),
]