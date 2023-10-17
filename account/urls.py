from django.urls import path
from .views import Admin

urlpatterns = [
    path('api/admin/<int:pk>/', Admin.as_view(), name='admin'),
]
