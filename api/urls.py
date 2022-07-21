from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.GetApiOverview.as_view(), name='api-overview'),
    path('users/', include('users.urls'))
]