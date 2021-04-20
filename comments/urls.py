from django.urls import path

from . import views as my_views

urlpatterns = [
    path('<int:comment_pk>/delete/', my_views.CommentDeleteView.as_view(), name='comment_delete'),
    path('<int:comment_pk>/edit/', my_views.CommentUpdateView.as_view(), name='comment_update'),
    path('new/', my_views.comment_create_view, name='comment_create'),
    path('<int:comment_pk>/', my_views.CommentDetailView.as_view(), name='comment_detail'),
]