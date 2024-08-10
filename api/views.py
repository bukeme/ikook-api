from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking
from .permissions import IsMenuChef, IsUserRole


class MenuAPIViewSet(ModelViewSet):
	serializer_class = MenuSerializer
	permission_classes = [IsAuthenticated, IsMenuChef]

	def get_queryset(self):
		return Menu.objects.filter(user__country=self.request.user.country)

	def perform_create(self, serializer):
		serializer.save(user=self.request.user)
		return super().perform_create(serializer)

class BookingAPIView(GenericAPIView, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
	serializer_class = BookingSerializer
	permission_classes = [IsAuthenticated, IsUserRole]

	def get(self, request, *args, **kwargs):
		if kwargs.get('pk'):
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def perform_create(self, serializer):
		if serializer.validated_data['menu'].user.country != self.request.user.country:
			raise PermissionDenied(detail='Menu is not available in your country')
		serializer.save(user=self.request.user)
		return super().perform_create(serializer)

	def get_queryset(self):
		return Booking.objects.filter(user__country=self.request.user.country)