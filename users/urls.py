from django.urls import path, include

from . import views as my_views

urlpatterns = [
    path('signup/', my_views.UserCreateView.as_view(), name='signup'),
    path('edit/', my_views.UserUpdateView.as_view(), name='user_update'),
    path('', include('django.contrib.auth.urls')),
]