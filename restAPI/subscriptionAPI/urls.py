from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subscriptionAPI import views

urlpatterns = [
    path('login/',views.AuthenticateUserView.as_view()), # POST request
    path('signup/',views.CreateUserView.as_view()), # POST request
    path('managerdetails/all/',views.ManagerDetailsView.as_view()),  # GET request
    path('subscriptions/',views.SubscriptionDetailView.as_view()) # GET request to get all data , POST request to add data
]

urlpatterns = format_suffix_patterns(urlpatterns)