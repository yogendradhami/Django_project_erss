from django.shortcuts import render
from .serializers import  EmployeeSerializer
from app_employeewebsite.models import Employee,Department

from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
from rest_framework.views import APIView
from django.contrib.auth.models import  User


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
    
    def errorResponse(self, code, msg, error=dict()):
        context  = {
            "status_code": code,
            "message":msg,
            "data":[],
            "error":error
        }
        return context
    

class EmployeeApiView(APIView):
    def get(self, request):
        employee = Employee.objects.all()
        serializer= EmployeeSerializer(employee, many=True)
       
        return Response(CustomResponse.successResponse(200,"Employee List", serializer.data), status=status.HTTP_200_OK)
    

    def post(self,request):
        # user =User.objects.get(id=request.POST.get('user'))
        # departmet = Department.objects.get(id=request.POST.get('department'))
        # data = {
        # "full_name" =  request.POST.get('full_name')
        # "contact"  = request.POST.get('contact')
        # "email" = request.POST.get('email')
        # "dob" = request.POSt.get('dob')
        # "join_date"=request.POST.get('joint_date')
        # "gender"  = request.POST.get('gender')
        # "blood_group" = request.POST.get('blood_group')
        # "address"  = request.POST.get('address')
        # "user" = user
        # "department"= departmet
        # }
        # employee = Employee()
       


        serializer = EmployeeSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return render(CustomResponse.successResponse(200, "Added successfully", serializer.data), status = status.HTTP_200_OK)
        else:

            return Response(CustomResponse.errorResponse(200, "Validation Error", serializer.errors))

class EmployeeApiIdView(APIView):
    def get_object(self, id):
        try:
            data = Employee.objects.all(id=id)
            return data
        except Employee.DoesNotExist:
            return  None
        
    def get(self,request, id):
        instance  =self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EmployeeSerializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, requset, id):
        instance  =self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        serializer  = EmployeeSerializer(data=requset, instance=instance)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.errors,status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, id):
        instance  =self.get_object(id=id)

        if not instance:
            return Response({"msg":"Not Found"}, status=status.HTTP_404_NOT_FOUND)
        
        instance.delete()
        return Response({"msg":"Deleted successfully"}, status=status.HTTP_200_OK)