from django.contrib import admin

from profiles.models import Profile, OTPVerification

admin.site.register(Profile)
admin.site.register(OTPVerification)
