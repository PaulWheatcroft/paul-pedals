from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_bag, name='view_bag'),
    path('add/<item_id>/', views.add_to_bag, name='add_to_bag'),
    path('amend/<item_id>/', views.amend_to_bag, name='amend_to_bag'),
    path('remove/<item_id>/', views.remove_bag_item, name='remove_bag_item'),
]
