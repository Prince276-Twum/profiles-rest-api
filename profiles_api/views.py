from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
from rest_framework.viewsets import ViewSet, ModelViewSet
from profiles_api import models
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions
from rest_framework import filters

# Create your views here.


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, pk, format=None):
        print(pk)
        an_apiview = [
            "it uses http method as as a fuction",
            "is similar to tradtion django views",
            "gives your the most contol over your application"
        ]

        return Response({"message": "Hello", "an_apiview": an_apiview})

    def post(self, request, ):
        """CREA A HELLO MESSAGE"""
        print(request.data)
        serializer = self.serializer_class(data=request.data)
        print(serializer)
        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hello {name}"

            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        return Response({"method": "PUT"})

    def patch(self, request, pk=None):
        return Response({"method": "PATCH"})

    def delete(self, request, pk=None):
        return Response({"method": "DELETE"})


class HelloViewset(ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request, ):
        a_viewset = [

            "user action like list creat retrieve update patil update",
            "automatioccal map to url using router",
            "Provides more fountionality with less code"
        ]

        return Response({"message": "hello", "a_viewset": a_viewset})

    def create(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get("name")
            message = f"hello {name}"
            return Response({"message": message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({"http_mettod": "GET"})

    def update(self, request, pk=None):
        return Response({"http_mettod": "PUT"})

    def partial_update(self, request, pk=None):

        return Response({"http_mettod": "Patch"})

    def destroy(self, request, pk=None):

        return Response({"http_mettod": "Delete"})


class UserProfilViewset(ModelViewSet):
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "email",)
