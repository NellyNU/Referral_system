from rest_framework import serializers
from .models import User

class PhoneAuthSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)

class AuthCodeVerifySerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=4)

class UserProfileSerializer(serializers.ModelSerializer):
    invited_users = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['phone_number', 'invite_code', 'activated_invite_code', 'invited_users'] 

    def get_invited_users(self, obj):
        return [user.phone_number for user in obj.get_invited_users()]

class InviteActivationSerializer(serializers.Serializer):
    invite_code = serializers.CharField(max_length=6) 
