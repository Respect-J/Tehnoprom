from django.urls import path
from .views import BrandListView, BrandsByCategorySlug, BrandView

urlpatterns = [
    path("", BrandView.as_view(), name="Brand-get"),
    path('category/<slug:category_slug>/', BrandsByCategorySlug.as_view(), name='brand-categories'),
    path('categorybrands/', BrandListView.as_view(), name='brand-categories'),

]
