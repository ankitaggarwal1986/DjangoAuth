from django.urls import path
from . import views
from django.urls.resolvers import URLPattern

urlpatterns = [

    path('buyerlist/',views.BuyerList.as_view()),
    path('buyerdetail/<int:pk>',views.BuyerDetail.as_view()),
    path('machinelist/',views.MachineList.as_view()),
    path('machinedetail/<int:pk>',views.MachineDetail.as_view()),
    path('salelist/',views.SaleList.as_view()),
    path('saledetail/<int:pk>',views.SaleDetail.as_view()),

]