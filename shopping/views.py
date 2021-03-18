from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.base import TemplateView
from . import env as MyVars
from . import models as MyModels

class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ProductListView(ListView):
    model = MyModels.Producto
    template_name = 'products.html'
    context_object_name = 'productos'

class ProductDetailView(DetailView):
    model = MyModels.Producto
    template_name = 'product_detail.html'
    context_object_name = 'producto'

class ContactPageView(ListView):
    model = MyModels.Sucursal
    template_name = 'contact.html'
    context_object_name = 'sucursales'

class SoonPageView(TemplateView):
    template_name = 'soon.html'

class VersionPageView(TemplateView):
    template_name = 'version.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_version'] = MyVars.version
        context['version_title'] = MyVars.version_title
        context['version_description'] = MyVars.version_description
        context['changelog'] = MyVars.changelog
        return context