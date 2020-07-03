from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = [
    path('', router.urls),
    path('auth/', include('rest_framework.urls'), namespace='rest_framework')
]