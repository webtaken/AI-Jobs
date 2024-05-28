from django.urls import path

from .views import companies, index

app_name = "app"
urlpatterns = [
    path("", index, name="index"),
    path("companies", companies, name="companies"),
]
