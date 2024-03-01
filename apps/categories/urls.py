from django.urls import path

from .views import CategoryListView, CategoryRetrieveUpdateDelete, CategoriesByCollectionUUID

urlpatterns = [
    path("", CategoryListView.as_view(), name="Category-get-create"),
    path('collections/<uuid:collection_id>/', CategoriesByCollectionUUID.as_view(), name='collection-categories'),
    path("<uuid:pk>/", CategoryRetrieveUpdateDelete.as_view(), name="Category-retrieve-update-delete"),
]
