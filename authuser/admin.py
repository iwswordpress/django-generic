from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile


class AccountAdmin(UserAdmin):
    # Columns in User
    list_display = ('email','first_name','last_name')
    search_fields = ('email',)
    # We need to make password readonly...
    readonly_fields = ('password',)


admin.site.register(User, AccountAdmin)
admin.site.register(Profile)

