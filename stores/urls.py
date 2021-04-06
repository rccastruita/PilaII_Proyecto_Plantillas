from django.urls import path

from . import views as my_views

urlpatterns = [
    path('list/', my_views.StoreListView.as_view(), name='store_list'),
    path('new/', my_views.StoreCreateView.as_view(), name='store_create'),
    path('<int:pk>/edit/', my_views.StoreUpdateView.as_view(), name='store_update'),
    path('<int:pk>/delete/', my_views.StoreDeleteView.as_view(), name='store_delete'),
]