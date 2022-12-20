
from django.urls import path
from . import views

urlpatterns = [
    path('getUsers', views.listAllUsers),
    path('addUser',views.addUser),
    path('updateUser/<id>/',views.updateUser),
    path('getBookings',views.listAllBookings),
    path('getUser/<id>/',views.getUser),
    path('getBooking/<booking_uuid>/',views.getBooking)
]