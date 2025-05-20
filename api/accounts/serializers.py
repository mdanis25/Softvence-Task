from accounts.models import CustomUser 
from rest_framework import serializers 
from django.contrib.auth import authenticate

class CustomUserSerializer(serializers.ModelSerializer): 
    class Meta: 
        model = CustomUser 
        fields = ['id', 'username', 'email']

class UserRegistrationSerializer(serializers.ModelSerializer): 
    password1 = serializers.CharField(write_only = True)
    password2 = serializers.CharField(write_only = True)

    class Meta: 
       model = CustomUser  
       fields = ['id', 'username', 'email', 'password1', 'password2'] 
       extra_kwargs = {'password': {'write_only' : True}} 
       
    def validate(self, attrs): 
        if attrs['password1'] != attrs['password2']:
            raise serializers.ValidationError('Password did not match!')  
        return attrs
    
    def create(self, validated_data): 
        password = validated_data.pop('password1') 
        validated_data.pop('password2') 
        
        return CustomUser.objects.create_user(password=password, **validated_data)
    
 
class UserLoginSerializer(serializers.Serializer):
    email = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get("email")
        password = data.get("password")

        if email and password:
            user = authenticate(username=email, password=password)
            if user and user.is_active:
                data['user'] = user
                return data
            raise serializers.ValidationError("Incorrect credentials!")
        else:
            raise serializers.ValidationError("Both email and password are required.")