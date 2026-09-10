from django.http import JsonResponse
from django.urls import include, path

urlpatterns = [
    path("health/", lambda request: JsonResponse({"status": "ok", "version": "0.1.0"})),
    path("api/", include("catalog.urls")),
]
