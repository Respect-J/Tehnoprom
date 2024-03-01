from django.urls import path

from .views import BannersListView, BannersRetrieveUpdateDelete

urlpatterns = [
    path("", BannersListView.as_view(), name="banners-list-create"),
    path("<uuid:pk>/", BannersRetrieveUpdateDelete.as_view(), name="banners-retrieve-update-delete"),
]
