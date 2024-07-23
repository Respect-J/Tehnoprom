from django.urls import path

from .views import CollectionListView

urlpatterns = [
    path("", CollectionListView.as_view(), name="collections-get-create")
]
