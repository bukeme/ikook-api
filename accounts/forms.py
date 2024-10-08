from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('role', 'country', 'username',)

class CustomUserChangeForm(UserChangeForm):
	class Meta:
		model = User
		fields = ('role', 'country', 'username')