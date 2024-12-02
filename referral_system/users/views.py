from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import login
import random
import time
from django.core.cache import cache
from .models import User, AuthCode
from.serializers import PhoneAuthSerializer, AuthCodeVerifySerializer, UserProfileSerializer,InviteActivationSerializer

# Create your views here.

class PhoneAuthView(APIView):
    def post(self, request):
        serializer = PhoneAuthSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']

            auth_code = str(random.randint(1000,9999))
            cache.set(f'auth_code_{phone_number}', auth_code , 180)
            print(f"Код авторизации для {phone_number}: {auth_code}")
            return Response({'message': 'Код отправлен'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyAuthCodeView(APIView):
    def post(self, request):
        serializer = AuthCodeVerifySerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            code = serializer.validated_data['code']

            cached_code = cache.get(f'auth_code_{phone_number}')
            if cached_code and cached_code == code:
                user, created = User.objects.get_or_create(phone_number=phone_number)
                cache.delete(f'auth_code_{phone_number}')
                login(request, user)
                return Response({'error': 'Неверный код'}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)
    def post(self, request):
        serializer = InviteActivationSerializer(data=request.data)
        if serializer.is_valid():
            invite_code = serializer.validated_data['invite_code']
            try:
                invited_user = User.objects.get(invite_code=invite_code)

                if request.user.activated_invite_code:
                    return Response(
                        {'error': 'Вы уже активировали инвайт-код'},
                        status=status.HTTP_400_BAD_REQUEST
                    )

                request.user.activated_invite_code = invite_code
                request.user.save()

                return Response({'message': 'Инвайт-код успешно активирован'})

            except User.DoesNotExist:
                return Response(
                    {'error': 'Инвайт-код не существует'},
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)