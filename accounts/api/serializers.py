from rest_framework import serializers
from django.contrib.auth import password_validation
# from accounts.models import *


from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        if 'password' in validated_data:
              user.set_password(validated_data['password'])
              user.save()
        return user

    def validate_password(self, value):
        password_validation.validate_password(value, self.instance)
        return value
    
    def validate(self, data):
        if not data.get('first_name'):
            raise serializers.ValidationError({'first_name': 'User must have a first name'})

        if not data.get('last_name'):
            raise serializers.ValidationError({'last_name': 'User must have a last name'})
        
        return super(UserSerializer, self).validate(data)