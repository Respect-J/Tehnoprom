from django.urls import path

from .views import BrandProductListView, CategoryProductListView, ProductListView, ProductDetailBySlugView, \
    BrandCategoryProductListView, PopularProductListView, DayProductListView

urlpatterns = [
    path("", ProductListView.as_view(), name="Product-get"),
    path("getproduct/<slug:slug>/", ProductDetailBySlugView.as_view(), name="Product-slug"),
    path("brand-category/<slug:brand_slug>/", BrandCategoryProductListView.as_view(), name="brands-catedory-products-list"),
    path("brands/<slug:brand_slug>/", BrandProductListView.as_view(), name="brands-products-list"),
    path("categories/<slug:category_slug>/", CategoryProductListView.as_view(), name="categories-products-list"),

    path("popular/", PopularProductListView.as_view(), name="popular-products-list"),
    path("dayproduct/", DayProductListView.as_view(), name="day-products-list"),
]
