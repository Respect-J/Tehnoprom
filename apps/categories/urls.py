from django.urls import path

from .views import CategoryListView, CategoriesByCollectionSlug, CollectionCategoryBrandView, PopularCategoryListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="Category-get-create"),
    path('collections/<slug:collection_slug>/', CategoriesByCollectionSlug.as_view(), name='collection-categories'),
    path('brands/collection/<slug:collection_slug>/', CollectionCategoryBrandView.as_view(),
         name='collection-category-brand-detail'),
    path("popular/", PopularCategoryListView.as_view(), name="popular-products-list"),
]
