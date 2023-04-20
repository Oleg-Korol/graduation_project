from django.conf.urls import url
from django.urls import path
from  rest_framework.urlpatterns import format_suffix_patterns

from .views import CarList
from .views import CarDetail

urlpatterns = [
      # url(r'^car/(?P<pk>\d +)?/?$',CarList.as_view()),
      path('car/',CarList.as_view()),
      path('car/<int:pk>/',CarDetail.as_view()),
         ]

urlpatterns = format_suffix_patterns(urlpatterns)