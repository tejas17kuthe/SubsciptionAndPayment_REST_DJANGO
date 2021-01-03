from rest_framework import serializers
from subscriptionAPI.models import ManagerDetails,SubscriptionDetatils,PaymentDetails,PaymentHistory
class ManagerDetailsSerializer(serializers.ModernSerializer):
    class Meta:
        model = ManagerDetails
        fields = ['email','first_name','last_name','password','address','dob','company']
        #or you can use 
        # fields = ['__all__']

class SubscriptionDetatilsSeializer(serializers.ModernSerializer):
    class Meta:
        model = SubscriptionDetatils
        fields = ['__all__'] # sub_id,subscription_name,amount,duration

        
class PaymentDetailsSeializer(serializers.ModernSerializer):
    class Meta:
        model = PaymentDetails
        fields = ['__all__'] # email,card_number,expire_month,expire_year


class PaymentHistorySeializer(serializers.ModernSerializer):
    class Meta:
        model = PaymentHistory
        fields = ['__all__'] # email,card_number,sub_id,amount,date_time
