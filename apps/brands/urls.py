from django.urls import path
from .views import BrandListView, BrandsByCategoriUUID, BrandView

urlpatterns = [
    path("", BrandView.as_view(), name="Brand-get"),
    path('category/<uuid:category_id>/', BrandsByCategoriUUID.as_view(), name='brand-categories'),
    path('categorybrands/', BrandListView.as_view(), name='brand-categories'),

]
