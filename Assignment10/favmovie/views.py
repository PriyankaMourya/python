from django.shortcuts import render
from django.http import HttpResponse
from . models import favmovie , buy
import json

# Create your views here.

def Findex(request):
    
    return render(request,"favmovie\home.html")

def Flist(request):
    # Courses = course.objects.all()
    AllCat = favmovie.objects.values("category") 
    cats = {var["category"] for var in AllCat }
    # for var in AllCat:
    # cats.append(var["category"])
    # cats = set(cats)    
    Favmovie = {}
    for val in cats:
        Favmovie[val] = favmovie.objects.filter(category=val)
    params = {
        "data": Favmovie
    }
    
    return render(request,"favmovie\index.html",params)


def Fdetails(request,id):
    # name = request.GET.get("id")

    try:
        params = {"data":favmovie.objects.get(id=id),"error":"null"}
    except:
        params = {"data":{},"error":"Movie not found"}

    return render(request,"favmovie\singlefavmovie.html", params)



def rent(request):
    str = request.POST.get("favsJson")
    favs = json.loads(str)
    currentfavs = favs


    totalPrice = 0 
    for id in favs:


        temp= favs[id]
        tempOb = favmovie.objects.get(id=id)
        price = tempOb.price
        temp["price"]=price
        temp["totalItemPrice"] = price * temp["value"]
        totalPrice = totalPrice + temp["totalItemPrice"]
        currentfavs[id] = temp 
    params = {
        "totalPrice" : totalPrice,
        "data": currentfavs
    }
    return render(request,"favmovie\rent.html",params)

def submitrent(request):
    if(request.method=="POST"):
        jsonfavs= request.POST.get("jsonfavs")
        first_name= request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        email= request.POST.get("email")
        address= request.POST.get("address")
        state= request.POST.get("state")
        zip= request.POST.get("zip")
        isSameBillingAddress= request.POST.get("isSameBillingAddress")
        if(isSameBillingAddress=="on"):
            isSameBillingAddress = True
        else:
            isSameBillingAddress = False
        newBuy = buy(jsonfavs=jsonfavs,email=email, first_name=first_name ,last_name=last_name,state=state,zip=zip,address=address,isSameBillingAddress=isSameBillingAddress)
        newBuy.save()
        return HttpResponse("Thank you for buying!!")
    else:
        return HttpResponse("You are on a wrong page. please <a href='/favmovie/list'>Click here</a> to add items")

    return HttpResponse("Thank you")