from django.urls import path



from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from .views import (Register,Logout, GETPUTUserView)

urlpatterns = [
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/register/', Register.as_view(), name='register'),
    path('api/logout/', Logout.as_view(), name='logout'),
    path('api/user/', GETPUTUserView.as_view(), name='user'),
]