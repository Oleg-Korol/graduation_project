
# Create your views here.
from rest_framework import filters
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView, GenericAPIView
from .serializers import CarsSerializer
from mainapp.models import Car
from .paginations import StandartPagination


class CarList(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['last_name', 'price']
    search_fields = ['car_name', 'last_name', 'year_of_release', 'price']
    ordering = ['car_name']
    pagination_class = StandartPagination


class CarDetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarsSerializer
