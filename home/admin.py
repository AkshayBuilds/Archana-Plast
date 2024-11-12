from django.contrib import admin
from home.models import *

class saveadmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','subject','message')

admin.site.register(save,saveadmin)