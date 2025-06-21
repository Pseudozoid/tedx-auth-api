from rest_framework.permissions import BasePermission

# Custom permission class that allows access only to users with the role "admin"
class IsAdminUserRole(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            hasattr(request.user, 'userprofile') and
            request.user.userprofile.role == 'admin'
        )
