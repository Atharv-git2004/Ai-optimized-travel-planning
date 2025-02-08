from django.db import models

# Create your models here.
class LoginTable(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    password=models.CharField(max_length=100,null=True,blank=True)
    usertype=models.CharField(max_length=100,null=True,blank=True)

class PackageTable(models.Model):
    packagename=models.CharField(max_length=50,null=True,blank=True)
    Details=models.CharField(max_length=200,null=True,blank=True)
    Duration=models.CharField(max_length=50,null=True,blank=True)
    Facility=models.CharField(max_length=200,null=True,blank=True)
    Price=models.FloatField(null=True,blank=True)

class FlightTable(models.Model):
    RouteNo=models.CharField(max_length=20,null=True,blank=True)
    PlaneNo=models.CharField(max_length=20,null=True,blank=True)
    DepartureDate=models.CharField(max_length=10,null=True,blank=True)
    DepartureTime=models.CharField(max_length=10,null=True,blank=True)
    DepartureLocation=models.CharField(max_length=50,null=True,blank=True)
    ArrivalTime=models.CharField(max_length=10,null=True,blank=True)
    ArrivalLocation=models.CharField(max_length=50,null=True,blank=True)
    TicketPrice=models.CharField(max_length=15,null=True,blank=True)

class HotelTable(models.Model):
    HotelName=models.CharField(max_length=50,null=True,blank=True)
    HotelType=models.CharField(max_length=30,null=True,blank=True)
    Location=models.CharField(max_length=100,null=True,blank=True)
    City=models.CharField(max_length=30,null=True,blank=True)
    Country=models.CharField(max_length=30,null=True,blank=True)
    NumberOfRooms=models.IntegerField(null=True,blank=True)
    Facilities=models.CharField(max_length=200,null=True,blank=True)
    PetPolicy=models.CharField(max_length=20,null=True,blank=True)
    ContactNo=models.BigIntegerField(null=True,blank=True)
    Email=models.CharField(max_length=50,null=True,blank=True)
    Website=models.CharField(max_length=100,null=True,blank=True)
    BasePrice=models.FloatField(null=True,blank=True)
    RoomType=models.CharField(max_length=30,null=True,blank=True)
    AdditionalFee=models.FloatField(null=True,blank=True)
    HotelStatus=models.CharField(max_length=20,null=True,blank=True)    
    CheckInTime=models.CharField(max_length=20,null=True,blank=True)
    CheckOutTime=models.CharField(max_length=20,null=True,blank=True)
    Description=models.CharField(max_length=250,null=True,blank=True)
    Images=models.FileField(upload_to='rooms/',null=True,blank=True)

class CustomerTable(models.Model):
    Username=models.CharField(max_length=30,null=True,blank=True)
    ContactNumber=models.BigIntegerField(null=True,blank=True)
    EmailID=models.CharField(max_length=30,null=True,blank=True)
        

class BookingTable(models.Model):
    UserID=models.ForeignKey(CustomerTable,on_delete=models.CASCADE,null=True,blank=True)
    Name=models.CharField(max_length=30,null=True,blank=True)
    Date=models.DateField(auto_now_add=True)
    BookingDetails=models.CharField(max_length=30,null=True,blank=True)
    ContactNumber=models.BigIntegerField(null=True,blank=True)
    Totalguests=models.IntegerField(null=True,blank=True)
    BookingStatus=models.CharField(max_length=30,null=True,blank=True)
    PaymentStatus=models.CharField(max_length=30,null=True,blank=True)
    Amount=models.FloatField(null=True,blank=True)


class AgencyTable(models.Model):
    AgencyName=models.CharField(max_length=30,null=True,blank=True)
    Location=models.CharField(max_length=30,null=True,blank=True)
    ContactPerson=models.CharField(max_length=30,null=True,blank=True)
    Email=models.CharField(max_length=30,null=True,blank=True)
    PhoneNo=models.BigIntegerField(null=True,blank=True)
    Services=models.CharField(max_length=150,null=True,blank=True)
    Destinations=models.CharField(max_length=150,null=True,blank=True)
    OperatingHours=models.IntegerField(null=True,blank=True)
    EstablishedYear=models.IntegerField(null=True,blank=True)
    Status=models.CharField(max_length=10,null=True,blank=True)

class FeedbackTable(models.Model):
    CustomerID=models.ForeignKey(CustomerTable,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(max_length=15,null=True,blank=True)
    Feedback=models.CharField(max_length=300,null=True,blank=True)

class PlacesTable(models.Model):
    Placename=models.CharField(max_length=30,null=True,blank=True)
    Spotname=models.CharField(max_length=30,null=True,blank=True)
    Category=models.CharField(max_length=30,null=True,blank=True)
    Description=models.CharField(max_length=30,null=True,blank=True)
    Image=models.FileField(upload_to='Places/',max_length=30,null=True,blank=True)
    
class RatingsAndReviewsTable(models.Model):
    CustomerID=models.ForeignKey(CustomerTable,on_delete=models.CASCADE,null=True,blank=True)
    AgencyID=models.ForeignKey(AgencyTable,on_delete=models.CASCADE,null=True,blank=True)
    Date=models.DateField(max_length=20,null=True,blank=True)
    Ratings=models.IntegerField(null=True,blank=True)
    Review=models.CharField(max_length=150,null=True,blank=True)

class GalleryTable(models.Model):
    AgencyID=models.ForeignKey(AgencyTable,on_delete=models.CASCADE,null=True,blank=True)
    GalleryImage=models.FileField(max_length=30,null=True,blank=True)




















  
           