from django.contrib import admin
from .models import PersonalInfo, NehasimModel, SendMailModel
# Register your models here.
admin.site.register(PersonalInfo)
admin.site.register(NehasimModel)
admin.site.register(SendMailModel)
