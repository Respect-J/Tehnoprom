from django.urls import path

from .views import BrandProductListView, CategoryProductListView, ProductListView, ProductRetrieveUpdateDelete, \
    BrandCategoryProductListView, PopularProductListView, DayProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="Product-get-create"),
    path("<uuid:pk>/", ProductRetrieveUpdateDelete.as_view(), name="Product-retrieve-update-delete"),
    path("brandscategory/<uuid:brand_id>/", BrandCategoryProductListView.as_view(), name="brands-products-list"),
    path("brands/<uuid:brand_id>/", BrandProductListView.as_view(), name="brands-products-list"),
    path("categories/<uuid:category_id>/", CategoryProductListView.as_view(), name="categories-products-list"),
    path("popular/", PopularProductListView.as_view(), name="popular-products-list"),
    path("dayproduct/", DayProductListView.as_view(), name="day-products-list"),
]
