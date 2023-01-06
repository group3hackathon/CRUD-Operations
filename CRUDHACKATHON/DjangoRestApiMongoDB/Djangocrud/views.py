from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Djangocrud.models import Department,Employee
from Djangocrud.serializers import DepartmentSerializer,EmployeeSerializer

# Create your views here.
def departmentApi(request, id=0):
    if request.method=='GET':
        department=Department.objects.all()
        department_serializer=DepartmentSerializer(department,many=True)
        return JsonResponse(department_serializer.data,safe=False)
    
    elif request.method=='POST':
        department_data=JSONParser().parse(request)
        department_serializer=DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successful",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Department.objects.get(DepartmentId=department_data['DepartmentID'])
        department_serializer=DepartmentSerializer(department,data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Update Succesfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        department=Department.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Deleted Succesfully",safe=False)

def EmployeeApi(request, id=0):
    if request.method=='GET':
        employees=Employee.objects.all()
        employees_serializer=EmployeeSerializer(employees,many=True)
        return JsonResponse(employees_serializer.data,safe=False)
    
    elif request.method=='POST':
        employee_data=JSONParser.parse(request)
        employees_serializer=EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successful",safe=False)
        return JsonResponse("Failed to Add",safe=False)
    elif request.method=='PUT':
        employees_data=JSONParser().parse(request)
        employees=Employee.objects.get(EmployeeId=employees_data['EmployeeID'])
        employees_serializer=EmployeeSerializer(employees,data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Update Succesfully", safe=False)
        return JsonResponse("Failed to Update")

    elif request.method=='DELETE':
        employees=Employee.objects.get(EmployeeId=id)
        employees.delete()
        return JsonResponse("Deleted Succesfully",safe=False)
        
 