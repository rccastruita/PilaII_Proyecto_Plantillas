from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy

from . import models as my_models

class StoreListView(ListView):
    model = my_models.Store
    context_object_name = 'stores'

class StoreCreateView(PermissionRequiredMixin, CreateView):
    permission_required = 'stores.add_store'

    model = my_models.Store
    template_name_suffix = '_create'
    fields = '__all__'
    success_url = reverse_lazy('store_list')

class StoreUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = 'stores.change_store'

    model = my_models.Store
    template_name_suffix = '_update'
    fields = '__all__'
    success_url = reverse_lazy('store_list')

class StoreDeleteView(PermissionRequiredMixin, DeleteView):
    permission_required = 'stores.delete_store'

    model = my_models.Store
    template_name_suffix = '_delete'
    context_object_name = 'store'
    success_url = reverse_lazy('store_list')