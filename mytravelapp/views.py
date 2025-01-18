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
    

     
    
        