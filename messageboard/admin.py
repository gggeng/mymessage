from django.contrib import admin
from .models import Msg

# Register your models here.

class MsgAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'datetime')


admin.site.register(Msg, MsgAdmin)