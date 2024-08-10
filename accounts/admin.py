from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from .forms import CustomUserCreationForm, CustomUserChangeForm

User = get_user_model()

# Register your models here.


class CustomUserAdmin(UserAdmin):
	form = CustomUserChangeForm
	add_form = CustomUserCreationForm
	model = User
	list_display = ('username', 'role', 'country', 'is_active', 'is_staff')
	list_filter = ('username', 'role', 'is_active', 'is_staff')
	fieldsets = (
		(None, {'fields': ('username', 'role', 'country', 'password')}),
		('Permissions', {'fields': ('is_active', 'is_staff', 'groups', 'user_permissions')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('username', 'role', 'country', 'usable_password', 'password'),	
		}),
	)
	search_fields = ('username',)
	ordering = ('username',)

admin.site.register(User, CustomUserAdmin)
