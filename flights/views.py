from rest_framework.generics import( DestroyAPIView,
RetrieveUpdateAPIView ,
ListAPIView ,
RetrieveAPIView ,
RetrieveUpdateAPIView
)
from datetime import datetime

from .models import Flight, Booking
from .serializers import (
UpdateSerializer,
DetailSerializer,
FlightSerializer,
BookingSerializer
)

class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gt=datetime.today())
	serializer_class = BookingSerializer

class BookingDetailsList(RetrieveAPIView):
	queryset = Booking.objects.all()
	serializer_class = DetailSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingUpdateList(RetrieveUpdateAPIView):
	queryset = Booking.objects.all()
	serializer_class = UpdateSerializer
	lookup_field = 'id'
	lookup_url_kwarg = 'booking_id'

class BookingDeleteList(DestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = DetailSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'booking_id'
