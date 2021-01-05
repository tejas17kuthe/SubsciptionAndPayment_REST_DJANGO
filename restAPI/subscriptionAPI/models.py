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
    duration = models.IntegerField(default=1)

