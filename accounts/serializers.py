from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegistrationSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ['pk', 'username', 'role', 'country', 'password']

	def create(self, validated_data):
		return User.objects.create_user(**validated_data)

class UserLogoutSerializer(serializers.Serializer):
	refresh = serializers.CharField()