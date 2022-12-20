from rest_framework import serializers
from main_app.models import Pyden_User,bookings



class ItemSerializer(serializers.ModelSerializer):
 class Meta:
  model=Pyden_User
  fields='__all__'

class BookingSerializer(serializers.ModelSerializer):
 class Meta:
  model=bookings
  fields='__all__'