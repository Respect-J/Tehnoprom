from django.urls import path

from .views import CharactericVIEW

urlpatterns = [
    path("<uuid:product_id>/", CharactericVIEW.as_view(), name="get-charasteric"),
]
