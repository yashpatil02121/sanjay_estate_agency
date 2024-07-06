from django.shortcuts import render, redirect, HttpResponse
from .models import Property, RentalProperty

# Create your views here.

def index(request):
    return render(request, "index.html")

def buy(request):
    properties = Property.objects.all()
    rentalproperties = RentalProperty.objects.all()
    context = {
        "properties":properties,
        "rentalproperties":rentalproperties,
    }
    
    return render(request, "buy.html",context)

def rent(request):
    if request.method=="POST":
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        room = request.POST.get("room")
        address = request.POST.get("address")
        landmark = request.POST.get("landmark")
        bhk = request.POST.get("bhk")
        bathroom = request.POST.get("bathroom")
        area = request.POST.get("area")
        price = request.POST.get("price")
        deposit = request.POST.get("deposit")
        furnished = request.POST.get("furnished")
        image = request.FILES.get("image")
        RentalProperty.objects.create(
            fullname=fullname,
            phone=phone,
            room=room,
            address=address,
            landmark=landmark,
            bhk=bhk,
            bathroom=bathroom,
            area=area,
            price=price,
            deposit=deposit,
            furnished=furnished,
            image=image
        )
        return redirect('rent')
    return render(request, "rent.html")

def sell(request):
    if request.method=="POST":
        fullname = request.POST.get("fullname")
        phone = request.POST.get("phone")
        room = request.POST.get("room")
        address = request.POST.get("address")
        landmark = request.POST.get("landmark")
        bhk = request.POST.get("bhk")
        bathroom = request.POST.get("bathroom")
        area = request.POST.get("area")
        price = request.POST.get("price")
        furnished = request.POST.get("furnished")
        image = request.FILES.get("image")
        Property.objects.create(
            fullname=fullname,
            phone=phone,
            room=room,
            address=address,
            landmark=landmark,
            bhk=bhk,
            bathroom=bathroom,
            area=area,
            price=price,
            furnished=furnished,
            image=image
        )
        return redirect('sell')
    return render(request, "sell.html")
