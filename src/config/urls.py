from django.urls import path, include

urlpatterns = [
    path("api/", include("wb_parser.urls")),
]
