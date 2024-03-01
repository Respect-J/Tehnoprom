from django.urls import path

from .views import ProductimegesListView, ProductIMGListView

urlpatterns = [
    path("", ProductIMGListView.as_view(), name="photos-list-create"),
    path("<uuid:product_id>/", ProductimegesListView.as_view(), name="products-img-list"),
]
