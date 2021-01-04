from django.shortcuts import render
from rest_framework.views import APIView
from subscriptionAPI.serializers import ManagerDetailsSerializer,SubscriptionDetatilsSeializer,PaymentDetailsSeializer,PaymentHistorySeializer,UserSerializer
from subscriptionAPI.models import ManagerDetails,SubscriptionDetails,PaymentDetails,PaymentHistory
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import status
from django.http import JsonResponse
import stripe 
# Create your views here.

stripe.api_key = 'sk_test_4eC39HqLyjWDarjtT1zdp7dc'

class ManagerDetailsView(APIView):
    """
    This view can only be accessed by admin user as it diplays all the details about the manager table
    Authenticate Request JSON format
    method type: GET
    url: /manaerdetails/all/
    {
       "username":"<Your user name>",
       "password":"< Your password >"
    }
    """
    permission_classes = [permissions.IsAdminUser]
    def get(self, request,format = None):
        details = ManagerDetails.objects.all()
        serialize = ManagerDetailsSerializer(details,many = True)
        return Response(serialize.data)

class SubscriptionDetailView(APIView):
    """
    Get all subscriptions
    method type: GET
    uri : /subscriptions/
    """
    def get(self,request,format = None):
        details = SubscriptionDetails.objects.all()
        serialize = SubscriptionDetatilsSeializer(details,many = True)
        return Response(serialize.data)

    """
    Add a subscription JSON format
    {
        "sub_id":"02",
        "subscription_name":"Super",
        "amount":"200",
        "duration":"1"
    }
    method type: POST
    uri : /subscriptions/
    """
    def post(self,request,format = None):
        serializer = SubscriptionDetatilsSeializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"New Subscription added successfully"},status = status.HTTP_202_ACCEPTED)
        else:
            return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

class AuthenticateUserView(APIView):
    """
    Authenticate Request JSON format 
    method type: POST
    url: /login/
    {
       "username":"<Your user name>",
       "password":"< Your password >"
    }
    """
    def post(self, request, format = None):
        resposne = {
            "details":"Your are successfully logged in."
        }
        return Response(resposne,status = status.HTTP_202_ACCEPTED)

class CreateUserView(APIView):
    """
        Create user Request Json format
        method type: POST
        url: /signup/
        {
            "email": "tejas@gmail.com",
            "first_name": "tejas",
            "last_name": "kuthe",
            "password": "123",
            "address": "nagpur",
            "dob": "1993-01-17",
            "company": "AT"
        },
        
    """

    permission_classes = [permissions.AllowAny]
    #Create new user
    def post(self,request,format = None):
        serializer_manager = ManagerDetailsSerializer(data = request.data) 
        #serializer = UserSerializer(data = request.data)
        if serializer_manager.is_valid():
            serializer_manager.save()
            username = serializer_manager.data['email']
            password = serializer_manager.data['password']
            first_name = serializer_manager.data['first_name']
            last_name = serializer_manager.data['last_name']
            user = User.objects.create_user(username=username,email=username,password=password,first_name = first_name,last_name=last_name)
            return Response({"User created Successfully"})
        else:
            return Response(serializer_manager.errors, status = status.HTTP_400_BAD_REQUEST)


