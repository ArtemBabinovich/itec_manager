from django.contrib import admin

from .models import CustomUser, Course, Group

admin.site.register(CustomUser)
admin.site.register(Course)
admin.site.register(Group)
