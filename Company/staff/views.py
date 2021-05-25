
from django.shortcuts import render,redirect,reverse
from .models import * 
from django.views.generic import ListView,CreateView
from .forms import *
# Create your views here.




class ListViewOfEmployee(ListView):
    queryset = Department.objects.all()
    context_object_name = 'department_list'
    template_name = 'EmployeeList.html'



def EmployeeTemplate(request):
	context = {}
	context['form'] = EmployeeForm
	Employee_data = Employee.objects.all()
	context['employee_list'] = Employee_data
	return render(request,'EmployeeData.html',context=context)


class EmployeeCreateView(CreateView):
	model = Employee
	fields = ['EmployeeName','Department']
	success_url = '/employee/create/screen/'

	def get_success_url(self):
		return reverse('EmployeeTemplate')