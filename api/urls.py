from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import MenuAPIViewSet, BookingAPIView

router = DefaultRouter()
router.register(r'menus', MenuAPIViewSet, basename='menus')
urlpatterns = [
	path('booking-list/', BookingAPIView.as_view(), name='booking_list'),
	path('booking-create/', BookingAPIView.as_view(), name='booking_create'),
	path('booking-retrieve/<int:pk>/', BookingAPIView.as_view(), name='booking_retrieve'),
]
urlpatterns += router.urls