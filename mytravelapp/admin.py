from django.contrib import admin

from mytravelapp.models import *

# Register your models here.
admin.site.register(LoginTable)
admin.site.register(PackageTable)
admin.site.register(FlightTable)
admin.site.register(HotelTable)
admin.site.register(CustomerTable)
admin.site.register(BookingTable)
admin.site.register(AgencyTable)
admin.site.register(FeedbackTable)
admin.site.register(PlacesTable)
admin.site.register(RatingsAndReviewsTable)
admin.site.register(GalleryTable)