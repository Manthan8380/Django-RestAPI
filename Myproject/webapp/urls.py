# from django.contrib import admin
from django.urls import path
from . views import employeesList, UserAPIView


urlpatterns = [
    path('employees/', employeesList.as_view()),
    path('employees/<str:pk>', employeesList.as_view()),
    path('user', UserAPIView.as_view())
]
