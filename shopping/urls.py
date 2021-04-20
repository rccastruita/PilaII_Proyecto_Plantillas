from django.urls import path, include
from . import views as MyViews

# Imports for serving media images on debug mode
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', MyViews.HomePageView.as_view(), name='home'),
    path('about', MyViews.AboutPageView.as_view(), name='about'),
    path('products', MyViews.ProductListView.as_view(), name='product_list'),
    path('products/<int:product_pk>/comments/', include('comments.urls')),
    path('products/<int:product_pk>/', MyViews.ProductDetailView.as_view(), name='product_detail'),
    path('soon', MyViews.SoonPageView.as_view(), name='soon'),
]

# url for serving media on debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)