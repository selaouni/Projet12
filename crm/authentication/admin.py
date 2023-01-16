from authentication.models import User
from django.contrib import admin

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email')

    def active(self, obj):
        return obj.is_active == 1

    active.boolean = True

admin.site.register(User,UserAdmin )
