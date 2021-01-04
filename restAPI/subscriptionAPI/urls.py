from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from subscriptionAPI import views

urlpatterns = [
    path('login/',views.AuthenticateUserView.as_view()),
    path('signup/',views.CreateUserView.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)