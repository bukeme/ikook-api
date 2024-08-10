from django.urls import path
from .views import UserRegistrationAPIView, UserLogoutAPIView


urlpatterns = [
	path('register/', UserRegistrationAPIView.as_view(), name='register'),
	path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]