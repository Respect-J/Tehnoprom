from django.urls import path
from .views import ProductListView, ProductRetrieveUpdateDelete, BrandProductListView, CategoryProductListView

urlpatterns = [
    path('', ProductListView.as_view(), name='Product-get-create'),
    path('<uuid:pk>/', ProductRetrieveUpdateDelete.as_view(), name='Product-retrieve-update-delete'),
    path('brands/<uuid:brand_id>/', BrandProductListView.as_view(), name='brands-products-list'),
    path('categories/<uuid:category_id>/', CategoryProductListView.as_view(), name='categories-products-list'),
]
