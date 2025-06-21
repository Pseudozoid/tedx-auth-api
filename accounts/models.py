from django.contrib.auth.models import User
from django.db import models

# UserProfile model to extend the built-in User model
# Adds a 'role' field for role-based access control
class UserProfile(models.Model):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
    )

    # One-to-one relationship with Django's built-in User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')

    def __str__(self):
        return f"{self.user.username} - {self.role}"

