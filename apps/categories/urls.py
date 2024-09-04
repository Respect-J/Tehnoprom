from django.urls import path

from .views import CategoryListView, CategoriesByCollectionUUID, CollectionCategoryBrandView, PopularCategoryListView

urlpatterns = [
    path("", CategoryListView.as_view(), name="Category-get-create"),
    path('collections/<uuid:collection_id>/', CategoriesByCollectionUUID.as_view(), name='collection-categories'),
    path('brands/collection/<uuid:collection_id>/', CollectionCategoryBrandView.as_view(),
         name='collection-category-brand-detail'),
    path("popular/", PopularCategoryListView.as_view(), name="popular-products-list"),
]
