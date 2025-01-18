"""
URL configuration for travelplan project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import  path
from mytravelapp.views import * 

urlpatterns = [
    path('', LoginPage.as_view(), name='login'),
    path('addplaces', AddPlaces.as_view(), name='addplaces'),
    path('manageflights', ManageFlights.as_view(), name='manageflights'),
    path('managehotels', ManageHotels.as_view(), name='managehotels'),
    path('manageplaces', ManagePlaces.as_view(), name='manageplaces'),
    path('managetravelagency', ManagetTravelagency.as_view(), name='managetravelagency'),
    path('reply', Reply.as_view(), name='reply'),
    path('viewfeedback', ViewFeedback.as_view(), name='viewfeedback'),
    path('viewpackages', ViewPackages.as_view(), name='viewpackages'),
    path('viewusers', ViewUsers.as_view(), name='viewusers'),
]
