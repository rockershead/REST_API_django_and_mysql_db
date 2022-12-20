from rest_framework.response import Response
from rest_framework.decorators import api_view
from main_app.models import Pyden_User,bookings
from .serializers import ItemSerializer,BookingSerializer


@api_view(['GET'])

def listAllUsers(request):
 users=Pyden_User.objects.all()   ##get everything
 serializer=ItemSerializer(users,many=True)
 return Response(serializer.data)

@api_view(['GET'])
def getUser(request,age):
 user=Pyden_User.objects.filter(age=age)
 #user=Pyden_User.objects.filter(age__gte=age)  ##for greater than
 serializer=ItemSerializer(user,many=True)
 ##add new json into database
 #new_user={"name":"Joe Black","age":32,"hobby":"piano"}
 #m = Pyden_User(**new_user)

 #m.save()
 
 return Response(serializer.data)

@api_view(['GET'])
def listAllBookings(request):
 booking=bookings.objects.all()   ##get everything
 serializer=BookingSerializer(booking,many=True)
 return Response(serializer.data)


@api_view(['GET'])
def getBooking(request,booking_uuid):
 booking=bookings.objects.filter(booking_uuid=booking_uuid)   ##get everything
 serializer=BookingSerializer(booking,many=True)
 return Response(serializer.data)


@api_view(['POST'])
def addUser(request):
 serializer=ItemSerializer(data=request.data)
 if serializer.is_valid():
  serializer.save()
 return Response('User created '+str(serializer.data))

@api_view(['PUT'])
def updateUser(request,id):
 try:
  user=Pyden_User.objects.get(id=id)
 except Pyden_User.DoesNotExist:
  return Response('404 NOT FOUND')
  
 
 
 serializer=ItemSerializer(user,data=request.data,partial=True)  ##must put partial=True!!!!
 
 if serializer.is_valid():
  serializer.save()
  return Response('User data updated')
 else:
  return Response('Error')
 
 
