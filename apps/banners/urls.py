from django.urls import path

from .views import BannersListView

urlpatterns = [
    path("", BannersListView.as_view(), name="banners-list-create")
]
