from django.urls import path
from .views import parser_view

urlpatterns = [
    path("parser/", parser_view, name="wb_parser"),

]
