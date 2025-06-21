from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import RegisterSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import CustomTokenObtainPairSerializer
from .permissions import IsAdminUserRole
from .models import UserProfile

# Handles user registration
class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()  # Saves user and auto-creates UserProfile
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Returns the authenticated user's profile data
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Ensure the user has a profile (creates one if missing)
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "role": profile.role,
        })

# Example protected endpoint for admin users only
class AdminOnlyView(APIView):
    permission_classes = [IsAdminUserRole]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

# Handles login and returns JWT access/refresh tokens
class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

# Redirect view for Google OAuth login
def google_login_redirect(request):
    token = request.session.pop('jwt_token', None)
    if token:
        # Redirect back to frontend with tokens in the query string
        url = f"http://localhost:8080/?access={token['access']}&refresh={token['refresh']}"
        return redirect(url)
    return JsonResponse({'error': 'No token generated'}, status=400)

# Admin-only endpoint to list all users and their roles
@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUserRole])
def list_users(request):
    users_data = []
    for user in User.objects.all():
        # Ensure every user has a corresponding profile
        profile, _ = UserProfile.objects.get_or_create(user=user)
        users_data.append({
            "username": user.username,
            "email": user.email,
            "role": profile.role
        })
    return Response(users_data)

