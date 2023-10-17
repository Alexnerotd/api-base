from django.urls import path, include


urlpatterns = [
    path("", include('user.urls')),
    path("", include('account.urls')),
    path("", include('blog.urls')),
]
