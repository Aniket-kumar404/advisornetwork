import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from adminapi.models import Advisor
from users.models import User, BookedCalls
from .serializers import UserCreateSerializer,BookingSerializer
from adminapi.serializers import AdvisorSerializer
# Create your views here.


class RegisterView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserCreateSerializer

    def post(self, request, format='json'):
        user_json_data = request.body
        stream = io.BytesIO(user_json_data)
        user_data = JSONParser().parse(stream)
        email = user_data.get('email')
        password = user_data.get('password')
        name = user_data.get('name')
        
        user = User.objects.create_user(email=email, name=name, password=password)
        user.save()
        return Response(status=status.HTTP_200_OK)


class AdvisorLists(APIView):
    permission_classes = [AllowAny]

    def get(self, request,id, format='json'):
        advisor_list = Advisor.objects.filter(id=id)
        Advisor_data = AdvisorSerializer(advisor_list, many=True)
        return Response(Advisor_data.data, status=status.HTTP_200_OK)

class BookedCall(APIView):
    permission_classes = [AllowAny]
    def post(self, request,user_id,advisor_id, format='json'):
        booked_calls =BookedCalls(user_id = user_id, advisor_id= advisor_id)
        booked_calls.save()
        return Response(status=status.HTTP_200_OK)


class Booking(APIView):
    permission_classes = [AllowAny]

    def get(self, request,user_id, format='json'):
        Booked = BookedCalls.objects.filter(user_id = user_id)
        for booked_data in Booked:
            advisor_id= booked_data.advisor_id
            time= booked_data.time
            id= booked_data.id
            advisor_list = Advisor.objects.filter(id=advisor_id)
            booking_data = BookingSerializer(id, time,many=True)
            Advisor_data = AdvisorSerializer(advisor_list, many=True)

            return Response(booking_data.data,Advisor_data.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
