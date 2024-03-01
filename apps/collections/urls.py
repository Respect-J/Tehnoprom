from django.urls import path
from .views import CollectionListView, CollectionRetrieveUpdateDelete

urlpatterns = [
    path('', CollectionListView.as_view(), name='collections-get-create'),
    path('<uuid:pk>/', CollectionRetrieveUpdateDelete.as_view(), name='collections-retrieve-update-delete')
]
