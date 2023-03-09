from django.shortcuts import render
from .serializers import  EmployeeSerializer
from app_employeewebsite.models import Employee

from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView


# Create your views here.
class CustomResponse():
    def successResponse(self, code, msg, data=dict()):
        context  = {
            "status_code": code,
            "message":msg,
            "data":data,
            "error":[]
        }
        return context
class EmployeeApiView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer= EmployeeSerializer(employee, many=True)
       
        return Response(CustomResponse.successResponse(200,"Employee List", serializer.data), status=status.HTTP_200_OK)

    def post(self,request):
        pass

class EmployeeApiIdView(APIView):
    def  get(self,request, id):
        pass

    def  putt(self, requset, id):
        pass

    def delete(self,request, id):
        pass