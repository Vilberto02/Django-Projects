from django.urls import path
from .views import IAGenerateView

urlpatterns = [
    path('consultar/', IAGenerateView.as_view(), name="consultar"),
]
