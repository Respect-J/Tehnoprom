from django.urls import path
from .views import BrandListView, BrandRetrieveUpdateDelete, BrandsByCategoriUUID

urlpatterns = [
    path("", BrandListView.as_view(), name="Brand-get-create"),
    path('category/<uuid:category_id>/', BrandsByCategoriUUID.as_view(), name='brand-categories'),
    path("<uuid:pk>/", BrandRetrieveUpdateDelete.as_view(), name="Brand-retrieve-update-delete"),
]
