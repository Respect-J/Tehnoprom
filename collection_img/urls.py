from django.urls import path
from .views import ProductIMGListView, ProductimegesListView

urlpatterns = [
    path('', ProductIMGListView.as_view(), name='photos-list-create'),
    path('<uuid:product_id>/', ProductimegesListView.as_view(), name='product-img-list'),

]
