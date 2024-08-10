from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()


def chef_role_only(pk):
	user = User.objects.get(pk=pk)
	if user.role != 'chef':
		raise ValidationError(f'The role of {user.username} is not "chef"')

def user_role_only(pk):
	user = User.objects.get(pk=pk)
	if user.role != 'user':
		raise ValidationError(f'The role of {user.username} is not "user"')