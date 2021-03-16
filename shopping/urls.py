from django.urls import path
from . import views as MyViews

# Imports for serving media images on debug mode
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MyViews.HomePageView.as_view(), name='home'),
    path('about', MyViews.AboutPageView.as_view(), name='about'),
    path('products', MyViews.ProductsPageView.as_view(), name='products'),
    path('products/<int:pk>/', MyViews.ProductDetailView.as_view(), name='product_detail'),
    path('soon', MyViews.SoonPageView.as_view(), name='soon'),
    path('contact', MyViews.ContactPageView.as_view(), name='contact'),
    path('version', MyViews.VersionPageView.as_view(), name='version'),
]

# url for serving media on debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)