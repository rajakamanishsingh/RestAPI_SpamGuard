from rest_framework import serializers
from .models import User, Contact,RandomNumber

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'phone_number', 'email','is_spam')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ('id', 'user', 'name', 'phone_number','email','is_spam')

class RandomNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model=RandomNumber
        fields = ('id','phone_number','is_spam')