from django.contrib import admin

# Register your models here.
from boldmann_profile.models import UserProfile

admin.site.register(UserProfile)
