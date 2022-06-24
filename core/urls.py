from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns

from core import views


urlpatterns = [
    path('', views.api_root),

    path('products/', views.ProductView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
]



urlpatterns = format_suffix_patterns(urlpatterns)