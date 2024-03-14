from django.contrib import admin
from .models import Tournament, WebUser, New
# Register your models here.
admin.site.register(Tournament)
admin.site.register(WebUser)
admin.site.register(New)