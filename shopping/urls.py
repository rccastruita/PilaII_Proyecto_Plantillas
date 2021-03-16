from django.urls import path

from . import views as MyViews

urlpatterns = [
    path('', MyViews.HomePageView.as_view(), name='home'),
    path('about', MyViews.AboutPageView.as_view(), name='about'),
    path('products', MyViews.ProductsPageView.as_view(), name='products'),
    path('soon', MyViews.SoonPageView.as_view(), name='soon'),
    path('contact', MyViews.ContactPageView.as_view(), name='contact'),
]