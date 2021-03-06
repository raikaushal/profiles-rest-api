from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """test API view
    """
    serializer_class=serializers.HelloSerializer

    def get(self,request,format=None):
        """Returns a list of APIview features"""
        an_apiview=[
            "a",
            "b",
            "c"
        ]

        return Response({'message':"hello","an_apiview":an_apiview})

    def post(self,request):
        """post request"""
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get("name")
            message=f"hello {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )

    def put(self,request,pk=None):
        """handles updating an object"""
        return Response({'method':'PUT'})

    def patch(self,request,pk=None):
        """handles partial updating an object"""
        return Response({'method':'PATCH'})

    def delete(self,request,pk=None):
        """handles delete method"""

        return Response({'method':'DELETE'})
