from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status, permissions
from .serializers import UserRegistrationSerializer, UserLogoutSerializer



class UserRegistrationAPIView(GenericAPIView):
	serializer_class = UserRegistrationSerializer

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			user = serializer.save()
			refresh = RefreshToken.for_user(user)
			return Response({
				**serializer.data,
				'tokens': {
					'refresh': str(refresh),
					'access': str(refresh.access_token)
				}
			}, status=status.HTTP_201_CREATED)

class UserLogoutAPIView(GenericAPIView):
	serializer_class = UserLogoutSerializer
	permission_classes = [permissions.IsAuthenticated]

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		if serializer.is_valid():
			refresh = serializer.data['refresh']
			RefreshToken(refresh).blacklist()
			return Response({}, status=status.HTTP_204_NO_CONTENT)
