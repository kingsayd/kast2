from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Accounnt

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','first_name','last_name','username','last_joind','date_joind','is_active')
    list_display_links = ('email','first_name','last_name')
    readonly_field =('last_joind','date_joind')
    ordaring = ('-date_joind',)  #show you discinding orders

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


admin.site.register(Accounnt,AccountAdmin)
