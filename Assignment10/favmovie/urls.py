from . import views
from django.urls import path 

urlpatterns = [
    
    path('',views.Findex),
    path('list/',views.Flist),
    path('detail/<int:id>',views.Fdetails),
    path('rent/',views.rent),
    path('submitrent/',views.submitrent),
    
]