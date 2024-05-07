# placement/admin.py
from django.contrib import admin
from .models import Internship, Placed, Placement

admin.site.register(Internship)
admin.site.register(Placement)
admin.site.register(Placed)



# myapp/admin.py

from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.models import User

class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource

admin.site.unregister(User)  # Unregister the default User admin
admin.site.register(User, UserAdmin)  # Register User with custom admin
