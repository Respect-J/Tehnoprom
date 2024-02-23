from django.urls import path
from .views import CategoryListView, CategoryRetrieveUpdateDelete

urlpatterns = [
    path('', CategoryListView.as_view(), name='Category-get-create'),
    path('<uuid:pk>/', CategoryRetrieveUpdateDelete.as_view(), name='Category-retrieve-update-delete')
]
