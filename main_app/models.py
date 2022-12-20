from django.db import models




class Pyden_User(models.Model):
 name=models.CharField(max_length=250)
 age=models.IntegerField()
 hobby=models.CharField(max_length=255,default='')


class bookings(models.Model):
 booking_uuid=models.CharField(max_length=250,primary_key=True)
 trip_uuid=models.CharField(max_length=250)
 reference=models.CharField(max_length=250)
 booked_by_user_uuid=models.CharField(max_length=250)
 booking_name=models.CharField(max_length=250)
 email=models.CharField(max_length=250)
 mobile_number=models.CharField(max_length=250)

 currency_code=models.CharField(max_length=250)
 transferred_trip_uuid=models.CharField(max_length=250)
 updated_by=models.CharField(max_length=250)
 class Meta:
  managed=False
  db_table='bookings'
