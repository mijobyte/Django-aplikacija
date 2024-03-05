from django.contrib import admin
from teretana.models import *
from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username"]
model_list = [Oznaka, Plan, Pretplatnik, Trener, Pretplata]
admin.site.register(model_list)