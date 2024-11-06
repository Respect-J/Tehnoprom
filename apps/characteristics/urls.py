from django.urls import path

from .views import CharactericView

urlpatterns = [
    path("<slug:product_slug>/", CharactericView.as_view(), name="get-charasteric"),
]
