from django.urls import path
from .views import PhoneAuthView,VerifyAuthCodeView,UserProfileView

urlpatterns = [
    path('auth/phone/', PhoneAuthView.as_view(), name='phone_auth'),
    path('auth/verify/', VerifyAuthCodeView.as_view(), name='verify_auth'),
    path('profile/', UserProfileView.as_view(), name='user_profile')
]