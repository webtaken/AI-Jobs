from django.urls import path

from .views import lead_company, set_alert

app_name = "alerts"

urlpatterns = []

htmx_patterns = [
    path("set_alert/", set_alert, name="set_alert"),
    path("lead_company/", lead_company, name="lead_company"),
]

urlpatterns += htmx_patterns
