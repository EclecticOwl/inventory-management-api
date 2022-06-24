from django.urls import path

from core import views


urlpatterns = [
    path('products/', views.ProductView.as_view()),
]