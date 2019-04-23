from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import UserSerializer
# Create your views here.


class UserCreate(APIView):

    def post(self, request):
        serialzer = UserSerializer(data=request.data)

        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors)


def reset(self, request):
    return HttpResponse('')