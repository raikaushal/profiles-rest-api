from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """test API view
    """

    def get(self,request,format=None):
        """Returns a list of APIview features"""
        an_apiview=[
            "a",
            "b",
            "c"
        ]

        return Response({'message':"hello","an_apiview":an_apiview})