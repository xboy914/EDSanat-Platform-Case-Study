from django.urls import include, path
from django.http import JsonResponse

urlpatterns = [
    path("health/", lambda request: JsonResponse({"status": "ok", "version": "0.1.0"})),
    path("api/", include("catalog.urls")),
]
