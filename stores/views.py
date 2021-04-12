from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models as my_models

class StoreListView(ListView):
    model = my_models.Store
    context_object_name = 'stores'

class StoreCreateView(CreateView):
    model = my_models.Store
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('store_list')

class StoreUpdateView(UpdateView):
    model = my_models.Store
    template_name_suffix = '_update'
    fields = '__all__'
    success_url = reverse_lazy('store_list')

class StoreDeleteView(DeleteView):
    model = my_models.Store
    template_name_suffix = '_delete'
    context_object_name = 'store'
    success_url = reverse_lazy('store_list')