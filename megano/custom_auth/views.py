from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from rest_framework import permissions

from . import serializers
from .models import Profile, Avatar
from .serializers import ProfileSerializer, PasswordSerializer, AvatarSerializer
import json

from django.db import IntegrityError



class SignInView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        username = user_data.get("username")
        password = user_data.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response(status=status.HTTP_201_CREATED)

        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SignUpView(APIView):
    def post(self, request):
        user_data = json.loads(request.body)
        name = user_data.get("name")
        username = user_data.get("username")
        password = user_data.get("password")
        print(user_data)

        try:
            user = User.objects.create_user(username=username, password=password)
            # profile = Profile.objects.create(user=user, first_name=name)
            Profile.objects.create(user=user, first_name=name)
            print(user_data)
            user = authenticate(request, username=username, password=password)
            print(user)
            if user is not None:
                login(request, user)

            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # try:
        #     user = User.objects.create_user(username=username, password=password)
        #     profile = Profile.objects.create(user=user, fullName=name)
        #     user = authenticate(request, username=username, password=password)
        #     if user is not None:
        #         login(request, user)
        #         return Response(status=status.HTTP_201_CREATED)
        #     else:
        #         return Response({'error': 'Failed to authenticate user.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        # except IntegrityError:
        #     return Response({'error': 'Username is already taken.'}, status=status.HTTP_400_BAD_REQUEST)
        # except serializers.ValidationError as e:
        #     return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        # except Exception as e:
        #     return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

def signOut(request):
    logout(request)
    return Response(status=status.HTTP_200_OK)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile)
        return Response(serializer.data)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        serializer = ProfileSerializer(profile, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            profile.user.email = request.data.get('email')
            profile.user.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfilePasswordView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        serializer = PasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            current_password = serializer.validated_data['currentPassword']
            new_password = serializer.validated_data['newPassword']
            if user.check_password(current_password):
                user.set_password(new_password)
                user.save()
                return Response(status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid current password.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileAvatarView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    # def post(self, request):
    #     profile = Profile.objects.get(user=request.user)
    #     avatar_serializer = AvatarSerializer(data=request.FILES["avatar"])
    #     if avatar_serializer.is_valid():
    #         avatar = avatar_serializer.save()
    #         profile.avatar = avatar
    #         profile.save()
    #         return Response(status=status.HTTP_200_OK)
    #     else:
    #         return Response(avatar_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        profile = Profile.objects.get(user=request.user)
        avatar = Avatar.objects.create(alt=f"avatar_{request.user.username}")
        avatar.src = request.FILES["avatar"]
        avatar.save()
        profile.avatar = avatar
        profile.save()
        return Response(status=status.HTTP_200_OK)