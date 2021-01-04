from django.shortcuts import render
from rest_framework.views import APIView
from subscriptionAPI.serializers import ManagerDetailsSerializer,SubscriptionDetatilsSeializer,PaymentDetailsSeializer,PaymentHistorySeializer,UserSerializer
from subscriptionAPI.models import ManagerDetails
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import status
from django.http import JsonResponse

# Create your views here.

class ManagerDetailsView(APIView):

    def get(self, request,format = None):
        details = ManagerDetails.objects.all()
        serialize = ManagerDetailsSerializer(details,many = True)
        return Response(serialize.data)

class AuthenticateUserView(APIView):
    def post(self, request, format = None):
        resposne = {
            "details":"Your are successfully logged in."
        }
        return Response(resposne,status = status.HTTP_202_ACCEPTED)

class CreateUserView(APIView):
    permission_classes = [permissions.AllowAny]
    #Create new user
    def post(self,request,format = None):
        serializer = UserSerializer(data = request.data)
        if serializer.is_valid():
            if not ManagerDetails.objects.filter(email = serializer.data['username']).exists() :
                
                print(serializeManager.data)
                return Response(serializer.data)
            else:
                return Response("Entry already exist Please signup with another email id")
        else:
            serializeManager = ManagerDetails.objects.get(email = serializer.data['username'])
            serializer = ManagerDetailsSerializer(serializeManager)
            return Response(serializer.data, status = status.HTTP_400_BAD_REQUEST)