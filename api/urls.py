from django.urls import path
from . import views


urlpatterns = [
    path('', views.GetApiOverview.as_view(), name='api-overview')
]