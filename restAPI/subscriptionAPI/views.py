from rest_framework.views import APIView
from subscriptionAPI.serializers import ManagerDetailsSerializer,SubscriptionDetatilsSeializer,UserSerializer
from subscriptionAPI.models import ManagerDetails,SubscriptionDetails
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework import status
from django.http import JsonResponse
from restAPI.settings import PAYU_MERCHANT_KEY, PAYU_MERCHANT_SALT
from django.template import Context, Template,RequestContext
from payu import gateway


# Create your views here
YOUR_DOMAIN = 'http://localhost:8000'
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
        
        if serializer_manager.is_valid():
            serializer_manager.save()
            username = serializer_manager.data['email']
            password = serializer_manager.data['password']
            first_name = serializer_manager.data['first_name']
            last_name = serializer_manager.data['last_name']
            User.objects.create_user(username=username,email=username,password=password,first_name = first_name,last_name=last_name)
            return Response({"User created Successfully"})
        else:
            return Response(serializer_manager.errors, status = status.HTTP_400_BAD_REQUEST)


import uuid

#Generating hash key for sending the data to payu server.
class PaymentGenerateHashView(APIView):
    permission_classes = [permissions.AllowAny]
    
    def post(self,request):
        data = request.data
        txnid = uuid.uuid1()
        data['txnid'] = txnid
        key = PAYU_MERCHANT_KEY
        salt = PAYU_MERCHANT_SALT
        PAYU_BASE_URL = gateway.payu_url() 
        action = PAYU_BASE_URL
        data['hash'] = gateway.get_hash(data) # get Hash
        data['action'] = action
        data['key'] = key
        return Response(data)
        
#Check if your transaction which is performed is same as the we sent to the payu server.
#This function accepts the json object received from payu after performing 
#the trandaction
#/confirmtransaction/
#This view internally stores data into payu.transaction table in the database
#This entry is important for further executions like cancel transaction , refund etc.
class ConfirmTransactionView(APIView):

    def post(self,request):
        if gateway.check_hash(request.data):
            return Response({"Transaction has been Successful."})
        else:
            return Response({"Transaction has been Failed."})

#Verify the status of the transaction
class VerifyTransactionView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        data = request.data
        return Response(gateway.verify_payment(data['txnid']))

    # Example Successful Response
    """
    {
        "status":1,"msg":"Transaction Fetched Successfully", 
        "transaction_details": {"mihpayid": "MIHPayID","request_id":"","bank_ref_num":"Bank Reference Number",
                                "amt":"Amount", "disc":"Discount","mode":"Transaction Mode (NB for Netbanking, CC for credit card, DC for Debit card, '-' for unknown)",
                                "status":"Transaction Status"}
    }
    """


class CancelTransactionView(APIView):
    
    def post(self,request):
        response = gateway.cancel_transaction(request.data["mihpayid"], request.data["Amount"])
        return response
    # Example Successful Responses
    """
        {"status": 1, "msg": "Cancel Request Queued", "request_id": "RequestID", "mihpayid": "MIHPayID", "bank_ref_num": "Bank Reference Number"}
    """

    # Example Failure Response
    """
        {"status": 0, "msg":"Cancel request failed"}
    """

#This is used for request for refund by passing the mahpayid and amount. These values should be reveived from the 
# payu.transaction database
class RefundTransactionView(APIView):
    
    def post(self,request):
        return Response(gateway.refund_transaction(request.data["mahpayid"],request.data["amount"]))