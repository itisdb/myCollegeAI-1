from django.contrib import admin

from profiles.models import Profile, OTPVerification, Psychometry

admin.site.register(Profile)
admin.site.register(OTPVerification)
admin.site.register(Psychometry)
