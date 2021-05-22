from rest_framework import serializers
from users.models import User,BookedCalls

class UserCreateSerializer(serializers.ModelSerializer):

    class Meta():
        model = User
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):

    class Meta():
        model = BookedCalls
        fields = ('id','booking_time')

