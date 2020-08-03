from django.shortcuts import render
from django.shortcuts import render, redirect
from qrcode import *
from core.models import *
from django.contrib import messages



def HomeView(request):
    if request.user.is_authenticated:
        showqr = False
        airports = Airports.objects.all()
        stationS = Stations.objects.all()
        return render(request,'QRgenration.html', {'showqr': showqr, 'stationS':stationS,'airports':airports})
    else:
        return redirect('login')

def on_generate(request):
    try:
        if request.method=='POST':
            if request.user.is_authenticated:
                equip = request.POST['equipment_name']
                ariport =request.POST['airport_name']
                station = request.POST['station_name']
                serial = int(request.POST['serial_number'])
                modal = request.POST['modal_number']
                equipment_type = request.POST['equipment_type']
                if not Equipments.objects.filter(serial_number=serial).exists():
                    newoj_eq = Equipments(equipment_name=equip.upper(),
                    serial_number=serial,modal_number=modal,equipment_type=equipment_type )
                    newoj_eq.save()
                user = User.objects.filter(username=request.user.username).first()
                user_profile = Profile.objects.filter(user = user).first()
                data = equip+","+ariport+","+station+","+str(serial)+","+modal+","+equipment_type
                image_name = equipment_type+equip+modal
                qr=make(data)
                qr.save("static_files/media/"+image_name+".png")
                messages.info(request, "QR GENERATED SUCCESSFULLY🥳! Click On Show QR-Button To See.")
        showqr = True
        airports = Airports.objects.all()
        stationS = Stations.objects.all()
        context = {"data":data,'image_name': image_name, 'showqr':showqr, 
        'stationS':stationS
        ,'airports':airports}
        return render(request,"QRgenration.html", context)
    except Exception as E:
        print(E)
        messages.info(request, "Something Went Wrong!!")
        return redirect("/")


