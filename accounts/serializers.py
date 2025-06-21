
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.models import User

# Custom JWT serializer to allow login using either username or email
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username_or_email = attrs.get('username')
        password = attrs.get('password')

        # Try to find the user by username
        user = User.objects.filter(username=username_or_email).first()

        # If not found, try to find the user by email
        if user is None:
            user = User.objects.filter(email=username_or_email).first()

        # If still not found or password is incorrect, raise error
        if user is None or not user.check_password(password):
            raise serializers.ValidationError('Invalid username/email or password.')

        # Set the actual username so JWT can be issued properly
        attrs['username'] = user.username
        return super().validate(attrs)


# Serializer used for user registration
class RegisterSerializer(serializers.ModelSerializer):
    # Password should only be writeable, not readable
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    # Validate that email is unique
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("A user with this email already exists.")
        return value

    # Create and return a new user instance using the validated data
    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user

