from django.contrib import admin
from .models import Users, Requests, Articles, Content

# Register your models here.

admin.site.register(Users)
admin.site.register(Requests)
admin.site.register(Articles)
admin.site.register(Content)