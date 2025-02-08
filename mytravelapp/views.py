from http.client import HTTPResponse
from django.shortcuts import render # type: ignore
from django.views import View # type: ignore

from mytravelapp.models import LoginTable

# Create your views here.
class LoginPage(View):
    def get(self,request):
        return render(request,'login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=LoginTable.objects.get(username=username,password=password)
        request.session['user_id']=login_obj.id
        if login_obj.usertype=='admin':
            return HTTPResponse('''<script>alert('login successfully');window.location="/"</script>''')

# ///////////////////////////////////// ADMIN ////////////////////////////////////////////////////    
class AddPlaces(View):
    def get(self,request):
        return render(request,'addplaces.html')
    
class ManageFlights(View):
    def get(self,request):
        return render(request,'manageflights.html')
    
class ManageHotels(View):
    def get(self,request):
        return render(request,'managehotels.html')
    
class ManagePlaces(View):
    def get(self,request):
        return render(request,'manageplaces.html')
    
class ManagetTravelagency(View):
    def get(self,request):
        return render(request,'managetravelagency.html')

class Reply(View):
    def get(self,request):
        return render(request,'reply.html')

class ViewFeedback(View):
    def get(self,request):
        return render(request,'viewfeedback.html')
     
class ViewPackages(View):
    def get(self,request):
        return render(request,'viewpackages.html')
    
class ViewUsers(View):
    def get(self,request):
        return render(request,'viewusers.html')
    
class AddFlights(View):
    def get(self,request):
        return render(request,"addflights.html")
    
class AddHotels(View):
    def get(self,request):
        return render(request,"addhotels.html")
    
class ViewBookingsOfUsers(View):
    def get(self,request):
        return render(request,"viewbookingsofusers.html")
    
class Home(View):
    def get(self,request):
        return render(request,"home.html")
    

 # ///////////////////////////////// TRAVEL AGENCY //////////////////////////////////
  
class AddPackage(View):
    def get(self,request):
        return render(request,"travelagency/addpackage.html")

class AddPlaces(View):
    def get(self,request):
        return render(request,"travelagency/addplaces.html")
    
class GalleryManagement(View):
    def get(self,request):
        return render(request,"travelagency/gallerymanagement.html")
    
class Home(View):
    def get(self,request):
        return render(request,"travelagency/home.html")
    
class ManagePackage(View):
    def get(self,request):
        return render(request,"travelagency/managepackage.html")

class ManagePlaces(View):
    def get(self,request):
        return render(request,"travelagency/manageplaces.html")
    
class ProfileManagementt(View):
    def get(self,request):
        return render(request,"travelagency/profilemanagement.html")
    
class RatingAndReview(View):
    def get(self,request):
        return render(request,"travelagency/ratingandreview.html")
    
class Registration(View):
    def get(self,request):
        return render(request,"travelagency/registration.html")
    
class ViewBookings(View):
    def get(self,request):
        return render(request,"travelagency/viewbookings.html")
    
class ViewProfile(View):
    def get(self,request):
        return render(request,"travelagency/viewprofile.html")



    
        