from rest_framework_simplejwt.tokens import RefreshToken
from django.http import HttpResponseRedirect

def generate_jwt_for_user(backend, user, request, *args, **kwargs):
    if user:
        refresh = RefreshToken.for_user(user)
        access = str(refresh.access_token)
        return HttpResponseRedirect(f"https://tedx-auth-frontend.onrender.com?access={access}")

