from django import forms
from .models import *



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('EmployeeName','Department')