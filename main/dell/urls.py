import imp
from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns = [
    path('employeelist/',views.EmployeeList.as_view()),
    path('employeedetail/<int:pk>',views.EmployeeDetail.as_view()),
    path('trackinglist/',views.TrackingList.as_view()),
    path('trackingdetail/<int:pk>',views.TrackingDetail.as_view()),


]

