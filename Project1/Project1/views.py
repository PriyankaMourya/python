from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("hello")

def home(request):
    params = {}
    return render(request, "form.html", params)
    # return HttpResponse("yo <a href='/first'>first</a>" )
    
def main(request):
    params = {}
    return render(request, "formmain.html", params)

def showname(request):
    print(request.GET.get("first_name"))
    params = {
            "first_name":request.GET.get("first_name"),
            "last_name":request.GET.get("last_name"),
            "num":request.GET.get("num"),
            "email":request.GET.get("email"),
            "pass":request.GET.get("pass"),
            "dob":request.GET.get("dob"),
            "yt":request.GET.get("yt"),
            
            # "showplace":request.GET.get("showplace", "off")
          
              }
    # return HttpResponse("<h1> First Name: " + params["first_name"] + "</h1>")
    return render(request, "formdata.html", params)