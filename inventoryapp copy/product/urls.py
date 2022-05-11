from django.conf.urls.static import static
from django.urls import path

from inventory_project import settings
from product.views import ProductList, ProductDetail, CreateProduct, UpdateProduct, DeleteProduct

urlpatterns = [
    path('', ProductList.as_view(), name='product_list'),
    path('<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    path('createproduct/', CreateProduct.as_view(), name='product_create'),
    path('<int:pk>/updateproduct', UpdateProduct.as_view(), name='product_update'),
    path('<int:pk>/deleteproduct', DeleteProduct.as_view(), name='product_delete'),
]

