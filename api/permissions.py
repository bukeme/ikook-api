from rest_framework.permissions import BasePermission


class IsMenuChef(BasePermission):
	message = 'You are not allowed to update this menu'

	def has_permission(self, request, view):
		if request.method == 'POST':
			return request.user.role == 'chef'
		return True

	def has_object_permission(self, request, view, obj):
		if request.method in ['PUT', 'PATCH', 'DELETE']:
			return obj.user == request.user
		return True

class IsUserRole(BasePermission):
	message = 'Your role is not "user."'

	def has_permission(self, request, view):
		if request.method == 'POST':
			return request.user.role == 'user'
		return True