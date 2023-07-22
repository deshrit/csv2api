from django.core import exceptions
from django.contrib.auth.password_validation import validate_password as django_pass_validation

from rest_framework import serializers
from .models import CustomUser


class SignupSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]
        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }
    
    def validate_password(self, password):
        
        try:
            django_pass_validation(password)
        except exceptions.ValidationError as e:
            raise serializers.ValidationError(e)
        
        return password