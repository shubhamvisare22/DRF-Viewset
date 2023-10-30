from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializers


class EmployeeViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializers(data=queryset, many=True)
        serializer.is_valid()
        return Response({'msg': 'All employee data fetched', 'data': serializer.data})

    def create(self, request):
        data = request.data
        serializer = EmployeeSerializers(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response({'data': 'Employee created...'})
        else:
            return Response({'data': serializer.errors})

    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializers(employee)
        return Response({'msg': 'Selected employee data fetched', 'data': serializer.data})

    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializers(instance=employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Employee updated...'})
        else:
            return Response({'msg': serializer.errors})

    def partial_update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializers(instance=employee, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Employee parially updated...'})
        else:
            return Response({'msg': serializer.errors})

    def destroy(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        if employee:
            employee.delete()
            return Response({'msg': 'Employee Deleted...'})
