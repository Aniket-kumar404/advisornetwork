from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# Create your views here.

class AdvisorView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, format='json'):
        return Response(status=status.HTTP_200_OK)
