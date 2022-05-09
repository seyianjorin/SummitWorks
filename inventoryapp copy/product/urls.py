from django.urls import path
from product.views import list_of_products, product_detail, product_from_user, update_product

urlpatterns = [
    path('', list_of_products),
    path('<int:id>/', product_detail),
    path('newproduct/', product_from_user),
    path('<int:id>/updateproduct', update_product)
]

