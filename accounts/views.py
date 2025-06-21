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

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        profile, _ = UserProfile.objects.get_or_create(user=request.user)
        return Response({
            "username": request.user.username,
            "email": request.user.email,
            "role": profile.role,
        })

class AdminOnlyView(APIView):
    permission_classes = [IsAdminUserRole]

    def get(self, request):
        return Response({"message": "Hello, Admin!"})

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

def google_login_redirect(request):
    token = request.session.pop('jwt_token', None)
    if token:
        # redirect back to frontend with token in query params
        url = f"http://localhost:8080/?access={token['access']}&refresh={token['refresh']}"
        return redirect(url)
    return JsonResponse({'error': 'No token generated'}, status=400)

@api_view(['GET'])
@permission_classes([IsAuthenticated, IsAdminUserRole])
def list_users(request):
    users = User.objects.all()
    data = [
        {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "role": getattr(user.userprofile, 'role', 'user')
        }
        for user in users
    ]
    return Response(data)
