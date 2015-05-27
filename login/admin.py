from django.contrib import admin

# Register your models here.
from .models import myUsers

admin.site.register(myUsers)