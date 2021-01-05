from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subscriptionAPI import views

urlpatterns = [
    path('login/',views.AuthenticateUserView.as_view()), # POST request
    path('signup/',views.CreateUserView.as_view()), # POST request
    path('managerdetails/all/',views.ManagerDetailsView.as_view()),  # GET request
    path('subscriptions/',views.SubscriptionDetailView.as_view()), # GET request to get all data , POST request to add data
    path('payment/',views.PaymentGenerateHashView.as_view() ),
    path('verifypayment/',views.VerifyTransactionView.as_view()),
    path('canceltransaction/',views.CancelTransactionView.as_view()),
    path('confirmtransaction/',views.ConfirmTransactionView.as_view()),
    path('refundpayment/',views.RefundTransactionView.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns)