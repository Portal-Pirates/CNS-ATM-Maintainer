from django.shortcuts import render
from django.contrib import messages
from core.models import *
import datetime

def getManagerProfile(request):
    user = request.user
    print(user)
    try:
        if Profile.objects.filter(name__iexact = user.username).first().is_manager:
            x = Profile.objects.filter(name__iexact = user.username).first()
            today = datetime.date.today()
            print(today)
            print(x.working_location)
            equipment_query = Equipments.objects.filter(station_name__iexact = x.working_location)
            if equipment_query:
                equipment_query_for_replacement = Equipments.objects.filter(replacement_date = today)
                equipment_query_for_maintainence = Equipments.objects.filter(maintainence_date = today)
                print(equipment_query_for_maintainence)
                print(equipment_query_for_replacement)
                return render(request,"manager.html",{"models":x,"replace":equipment_query_for_replacement,"maintainence":equipment_query_for_maintainence})
            else:
                messages.info(request,"No Equipment Found")
                return render(request,"index.html")
        else:
            messages.info(request,"You don't have manager permission")
            return render(request,"index.html")
    except Exception as e:
        print(e)
        return render(request,"index.html")
