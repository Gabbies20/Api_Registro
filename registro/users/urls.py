from django.urls import path
from .views import CreateUserView, UserListAPIView

urlpatterns = [
    path('register/', CreateUserView.as_view(), name='register'),
    path('api/user-list/', UserListAPIView.as_view(), name='user-list-api'),
]