from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from api.models import Company,Employee
from api.serializers import CompanySerializer,EmployeeSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializer



    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all().order_by()
    serializer_class=EmployeeSerializer
    

