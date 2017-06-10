from trips.models import Trip
from trips.serializers import TripSerializer
from django.http import Http404, JsonResponse
from rest_framework.views import APIView
from rest_framework import status
import pdb


class TripList(APIView):
    """
    List all trips, or create a new trip.
    """
    def get(self, request, format='json'):
        # current_user = request.user
        # TODO: get trip by user
        trips = Trip.objects.all()
        serializer = TripSerializer(trips, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request, format='json'):
        serializer = TripSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

class TripDetail(APIView):
    """
    Retrieve, update or delete a trip instance.
    """
    def get_object(self, pk):
        try:
            return Trip.objects.get(pk=pk)
        except Trip.DoesNotExist:
            raise Http404

    def get(self, request, pk, format='json'):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip)
        return JsonResponse(serializer.data, safe=False)

    def put(self, request, pk, format='json'):
        trip = self.get_object(pk)
        serializer = TripSerializer(trip, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST, safe=False)

    def delete(self, request, pk, format='json'):
        trip = self.get_object(pk)
        trip.delete()
        return JsonResponse(status=status.HTTP_204_NO_CONTENT, safe=False)
