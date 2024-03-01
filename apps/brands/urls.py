from django.urls import path
from .views import BrandListView, BrandRetrieveUpdateDelete

urlpatterns = [
    path('', BrandListView.as_view(), name='Brand-get-create'),
    path('<uuid:pk>/', BrandRetrieveUpdateDelete.as_view(), name='Brand-retrieve-update-delete')
]
