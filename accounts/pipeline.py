from rest_framework_simplejwt.tokens import RefreshToken

def generate_jwt_for_user(backend, user, request, *args, **kwargs):
    if user and request:
        refresh = RefreshToken.for_user(user)
        request.session['jwt_token'] = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

