from django.contrib import admin
from .models import *
# Register your models here.




class EmployeeAdmin(admin.ModelAdmin):

    fields = ['EmployeeName','Department','Email','DateOfBirth','Picture']
    list_display = ('EmployeeName','Department','Email','DateOfBirth')
    list_filter = ('Department','DateOfBirth')
    search_fields = ('Department','DateOfBirth')
admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department)