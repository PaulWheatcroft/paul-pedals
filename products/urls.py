from django.urls import path
from . import views

urlpatterns = [
    path('', views.products_view, name='products'),
    path('', views.products_view, name='products_view'),
    path('<product_id>', views.product_detail, name='product_detail'),
]
