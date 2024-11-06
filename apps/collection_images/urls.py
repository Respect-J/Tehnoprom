from django.urls import path

from .views import ProductimegesListView

urlpatterns = [
    path("<slug:product_slug>/", ProductimegesListView.as_view(), name="products-img-list"),
]
