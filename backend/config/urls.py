from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("health/", lambda request: JsonResponse({"status": "ok", "version": "1.0.0"})),
    path("api/auth/", include("accounts.urls")),
    path("api/orders/", include("orders.urls")),
    path("api/", include("catalog.urls")),
]
