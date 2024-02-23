from django.urls import path
from .views import CategoryListView, CategoryRetrieveUpdateDelete

urlpatterns = [
    path('', CategoryListView.as_view(), name='collection-get-create'),
    path('<uuid:pk>/', CategoryRetrieveUpdateDelete.as_view(), name='collection-retrieve-update-delete')
]
