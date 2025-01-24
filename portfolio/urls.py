from django.urls import path
from portfolio.views import IndexView

app_name = "portfolio"

urlpatterns = [
        path("", IndexView.as_view(), name="index"),
]
