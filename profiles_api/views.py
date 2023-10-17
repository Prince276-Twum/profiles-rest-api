from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers
# Create your views here.


class HelloApiView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):

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
