from django.urls import path

from .views import CharactericView

urlpatterns = [
    path("<uuid:product_id>/", CharactericView.as_view(), name="get-charasteric"),
]
