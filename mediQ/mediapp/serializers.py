from rest_framework import serializers
from .models import User, Doctor, Appointment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        # extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     user = User.objects.create_user(
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #     )
    #     return user

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True}}

    # def create(self, validated_data):
    #     doctor = Doctor.objects.create_user(
    #         email=validated_data['email'],
    #         password=validated_data['password'],
    #         first_name=validated_data.get('first_name', ''),
    #         last_name=validated_data.get('last_name', '')
    #     )
    #     return doctor

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'



from rest_framework import serializers
from django.contrib.auth import authenticate

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        print(f"Email: {email}")
        print(f"Password: {password}")

        user = authenticate(email=email, password=password)
        print(f"User = {user}")
        if user is None:
            raise serializers.ValidationError('Invalid email or password.')

        return {
            'email': email,
            'password': password,
        }
