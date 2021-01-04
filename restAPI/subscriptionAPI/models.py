from django.db import models
# Create your models here.
class ManagerDetails(models.Model):
    email = models.EmailField(primary_key=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    password = models.CharField(max_length=512)
    address = models.CharField(max_length=1000)
    dob = models.DateField()
    company = models.CharField(max_length=50)

class SubscriptionDetails(models.Model):
    sub_id = models.IntegerField(primary_key=True)
    subscription_name = models.CharField(max_length=50)
    amount = models.IntegerField()
    duration = models.IntegerField()

class PaymentDetails(models.Model):
    email = models.ForeignKey(ManagerDetails,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=17)
    expire_month = models.CharField(max_length=2) # Here you will have to convert  value to in while using
    expire_year = models.CharField(max_length=2)

class PaymentHistory(models.Model):
    email = models.ForeignKey(ManagerDetails,on_delete=models.CASCADE)
    card_number = models.CharField(max_length=17)
    sub_id = models.ForeignKey(SubscriptionDetails,on_delete=models.CASCADE)
    amount = models.IntegerField()
    date_time = models.DateTimeField()


