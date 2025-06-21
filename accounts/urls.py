from django.urls import path
from .views import RegisterView, ProfileView, CustomLoginView, AdminOnlyView, google_login_redirect, list_users
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', RegisterView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('google/redirect/', google_login_redirect, name='google-redirect'),
    path('admin-area/', AdminOnlyView.as_view(), name='admin-area'),
    path('admin/users/', list_users, name='list-users'),
]

