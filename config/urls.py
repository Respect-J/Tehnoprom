"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.payment.payme.views import GeneratePayLinkAPIView, PaymeCallBackAPIView
from config.settings import SITE_URL

schema_view = get_schema_view(
    openapi.Info(
        title="Tehnoprom E-Commerce backend API",
        default_version="v1",
        description="OpenAPI swagger documentation",
        terms_of_service="https://www.yourapp.com/terms/",
        contact=openapi.Contact(email="respect@jasur.com"),
        license=openapi.License(name="MIT"),
    ),
    url=SITE_URL,
    public=True,
    permission_classes=[permissions.IsAuthenticated],
)


admin.site.site_header = "THE TEXNOPROM"
admin.site.site_title = "Административная панель"
admin.site.index_title = "Добро пожаловать в административную панель"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("banners/", include("apps.banners.urls")),
    path("orders/", include("apps.orders.urls")),
    path("collections/", include("apps.collections.urls")),
    path("categories/", include("apps.categories.urls")),
    path("products/", include("apps.products.urls")),
    path("brands/", include("apps.brands.urls")),
    path("photos/", include("apps.collection_images.urls")),
    path("users/", include("apps.users.urls")),
    path("uzum/", include("apps.payment.uzum.urls")),
    path('installment', include("apps.installment.urls")),
    path("characteristics/", include("apps.characteristics.urls")),
    path("payments/merchant/", PaymeCallBackAPIView.as_view()),
    path("pay-link/", GeneratePayLinkAPIView.as_view()),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    re_path(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
