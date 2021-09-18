from django.http import HttpResponse
from django.shortcuts import render


def home(request):
   return render(request,"index.html")
   



def show(request):
   
    params={
        "first_name" :request.POST.get("first_name") ,
        "last_name" :request.POST.get("last_name"),
        "p_no" :request.POST.get("p_no"),
        "dob" :request.POST.get("dob") ,
        "email" :request.POST.get("email"),
        "password" :request.POST.get("password"),
        "link": request.POST.get("link")
        
        
        }
   
    return render(request,"show.html",params)