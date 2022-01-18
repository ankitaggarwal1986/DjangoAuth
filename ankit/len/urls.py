from django.urls import path
from . import views

urlpatterns = [
    #path('', views.apiOverview, name='apioverview'),
    path('product-list/', views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>', views.ViewDetail, name='product-detail'),
    path('product-create/', views.Create, name='product-create'),
    path('product-update/<int:pk>', views.Update, name='product-update'),
    path('product-delete/<int:pk>', views.Delete, name='product-delete'),
    
]