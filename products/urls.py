from django.urls import path
from .views import(
  product_create_view,
  product_delete_view,
  product_detail_view,
  product_list_view,
  dynamic_lookup_view
)

urlpatterns=[
  path('', product_list_view),
  path('create/', product_create_view),
  path('<int:id>/', dynamic_lookup_view, name='product-detail'),
  path('<int:id>/delete/', product_delete_view, name='product-delete'),
]