from django.shortcuts import render
from django.views import generic
from rest_framework.serializers import ModelSerializer
from .models import MyUser, BikeModel, BlogModel, OurServices, ServiceRequestForm
from .serializer import MyUserSerializer, UserSerializer, BikeSerializer, BlogSerializer, OurServicesSerializer, ServiceRequestFormSerializer, ChangePasswordSerializer, PhoneModelSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.mixins import ListModelMixin
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# IMPORTING FOR KNOX AUTHENTICATION
from knox.models import AuthToken
from knox.views import LoginView
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from django.contrib.auth import login
from django.http import HttpResponse

# IMPORTING FOR MOBILE OTP
import os
from twilio.rest import Client

# IMPORTING OTP NEXT ATTEMPT
from datetime import datetime
from django.core.exceptions import ObjectDoesNotExist
import pyotp
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import phoneModel
import random

import os
from time import sleep
from simpleotp import OTP

# Create your views here.
class RegisterAPI(generics.GenericAPIView, ListModelMixin):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def get(self, request, *args, **kwargs):  
        return self.list(request, *args, **kwargs)

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            "user":UserSerializer(user).data,
            "token":AuthToken.objects.create(user)[1],
        }) 

class LoginAPI(LoginView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        user_data=super(LoginAPI, self).post(request,format=None)
        return user_data  
    
    def get(self, request, pk=None,format=None):
        userDatas = MyUser.objects.all() 
        userDatasSerializer = MyUserSerializer(userDatas, many=True)      
        return Response(userDatasSerializer.data)  

class BikeViewset(APIView):
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            bikedata = BikeModel.objects.get(id=id)
            serializer = BikeSerializer(bikedata)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        bikedatas = BikeModel.objects.all()
        serializer = BikeSerializer(bikedatas, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

    def put(self, request, pk, format=None):
        id = pk
        bikedata = BikeModel.objects.get(id=id)
        serializer = BikeSerializer(bikedata, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def patch(self, request, pk, format=None):
        id = pk
        bikedata = BikeModel.objects.get(pk=id)      
        serializer = BikeSerializer(bikedata, data=request.data, partial=True) 

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   
    
    def delete(self, request, pk=None, format=None):
        id=pk
        data = BikeModel.objects.get(id=id)      
        data.delete()
        return Response({'msg':'Data deleted'})  

class ServiceRequestFormViewset(APIView):
    def get(self, request, pk=None, format=None):
        id=pk
        if id is not None:
            serviceData = ServiceRequestForm.objects.get(id=id)
            serviceDataSerializer = ServiceRequestFormSerializer(serviceData)
            return Response(serviceDataSerializer.data)
        serviceDatas = ServiceRequestForm.objects.all()
        serviceDatasSerializer = ServiceRequestFormSerializer(serviceDatas, many=True)
        return Response(serviceDatasSerializer.data)

    def post(self, request, pk=None, format=None):
        serializer = ServiceRequestFormSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    
    def delete(self, request, pk=None, format=None):
        id=pk
        deletequery = ServiceRequestForm.objects.get(id=id)
        deletequery.delete() 
        return Response({'msg':'Record deleted successfully...'})  

    def put(self, request, pk, format=None):
        id = pk
        servicedata = ServiceRequestForm.objects.get(id=id)
        serviceserializer = ServiceRequestFormSerializer(servicedata, data=request.data)

        if serviceserializer.is_valid():
            serviceserializer.save()
            return Response(serviceserializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serviceserializer.errors, status=status.HTTP_400_BAD_REQUEST)  


class BlogViewSet(APIView):
    def get(self, request, pk=None,format=None):
        if pk is not None:
            blogData = BlogModel.objects.get(id=pk)
            blogDataSerializer = BlogSerializer(blogData)
            return Response(blogDataSerializer.data, status=status.HTTP_201_CREATED)
        blogdatas = BlogModel.objects.all()     
        blogdatasSerializer = BlogSerializer(blogdatas, many=True)   
        return Response(blogdatasSerializer.data)                
    
    def post(self, request, pk=None,format=None):
        serializer = BlogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)   


class OurServicesViewset(generics.GenericAPIView, ListModelMixin):
    queryset = OurServices.objects.all()
    serializer_class = OurServicesSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ChangePasswordView(generics.UpdateAPIView):
    # import pdb; pdb.set_trace();
    queryset = MyUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer  


def otpverify(pk, code):
    client = Client('', '')
    verify = client.verify.services('')
    verify.verifications.create(to=f'+977{pk}', channel='sms')

    result = verify.verification_checks.create(to=f'+977{pk}', code=code)
    print("OK = ",result.status)  

class SendOTP(APIView):
    def get(self, request, pk=None, code=None,format=None):
        print("OK TEST =  ", pk, code)
        otpverify(pk, code)
        return Response("ok", status=status.HTTP_201_CREATED)
       
    def post(self, request, pk=None, code=None):
        # import pdb; pdb.set_trace();
        client = Client('', '')
        verify = client.verify.services('')
        result = verify.verification_checks.create(to=f'+977{pk}', code=code)
        print("OK = ",result.status) 
        return Response("ok ok", status=status.HTTP_201_CREATED)
    


    
def otpv():
    client = Client('', '')
    verify = client.verify.services('')
    return verify

class SendOTPV(APIView):

    def get(self, request, pk=None, code=None,format=None):
        print("URL parameter =  ", pk, code)
        # import pdb; pdb.set_trace();
        try:   
            verify = otpv()
            verify.verifications.create(to=f'+977{pk}', channel='sms')
            # result = verify.verification_checks.create(to=f'+977{pk}', code=code)
            # print("OTP SEND = ", result.status)
            return Response("OTP sent", status=status.HTTP_201_CREATED)    
        except:   
            return Response("OTP Not Sent", status=status.HTTP_201_CREATED)


    def post(self, request, pk=None, code=None):
        phn = "+977{}"
        try:
            import pdb; pdb.set_trace();
            verify = otpv()
            result = verify.verification_checks.create(to=phn.format(pk), code=code)
            print("OTP CERIFICATION = ",result.status) 
            return Response("OTP Verified", status=status.HTTP_201_CREATED)
        except: 
            return Response("OTP Not Verified", status=status.HTTP_201_CREATED)        
#----------------------------------------------------------------------------------------------------------------
