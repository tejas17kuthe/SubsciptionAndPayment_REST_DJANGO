from rest_framework import serializers
from subscriptionAPI.models import ManagerDetails,SubscriptionDetails,PaymentDetails,PaymentHistory
from django.contrib.auth.models import User

class ManagerDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ManagerDetails
        fields = ['email','first_name','last_name','password','address','dob','company']
        #or you can use 
        # fields = ['__all__']

class SubscriptionDetatilsSeializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionDetails
        fields = ['sub_id','subscription_name','amount','duration'] # sub_id,subscription_name,amount,duration

        
class PaymentDetailsSeializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['__all__'] # email,card_number,expire_month,expire_year


class PaymentHistorySeializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = ['__all__'] # email,card_number,sub_id,amount,date_time


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id','username','password']