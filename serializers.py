from rest_framework import serializers
from App import models

"""
 sign up serializer validating and handeling the request data in user signup view
 we validate the user data , then if it's okay we call set_password method to hash his password
"""
class SignUpUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.AppUser
        fields = '__all__'


    def create(self, validated_data):
        user = super(SignUpUserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


