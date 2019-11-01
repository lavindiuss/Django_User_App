from django.shortcuts import render
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from App import serializers
from App import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from App import models
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import viewsets
import json



"""
 in post method we use signup serializer to handle the request data we got
 then if its valid we save user data and return its auth token
 __________

 in put method we make a partial update using our serializer by open partial option to True  
"""

class UserViews(APIView):
    permission_classes = (permissions.UserViewsPermissions,)
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        request = self.request
        serializer = serializers.SignUpUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            user = serializer.instance
            return Response(
                {"status": "created successfully",
                    "token": Token.objects.create(user=user).key
                 },
                status=status.HTTP_201_CREATED
            )

        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):

        usr = self.request.user
        serializer = serializers.SignUpUserSerializer(
            usr, data=self.request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

            return Response(
                {"status": "Updated successfully"},
                status=200
            )
        return Response(serializer._errors, status=status.HTTP_400_BAD_REQUEST)


class LogInView(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        }, status=200)


