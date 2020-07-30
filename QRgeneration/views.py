from django.shortcuts import render
from django.shortcuts import render, redirect
from qrcode import *
from core.models import *



def HomeView(request):
    if request.user.is_authenticated:
        showqr = False
        return render(request,'QRgenration.html', {'showqr': showqr})
    else:
        return redirect('login')

def on_generate(request):
    if request.method=='POST':
        if request.user.is_authenticated:
            equip = request.POST['equipment_name']
            ariport =request.POST['airport_name']
            station = request.POST['station_name']
            serial = request.POST['serial_number']
            modal = request.POST['modal_number']
            report_type = request.POST['equipment_type']
            user = User.objects.get(username=request.user)
            user_profile = Profile.objects.filter(user = user).first()
            data = equip+","+ariport+","+station+","+serial+","+modal+","+user_profile.name+","+report_type
            image_name = report_type+equip+modal
            qr=make(data)
            qr.save("static_files/media/"+image_name+".png")
    showqr = True
    return render(request,"QRgenration.html",{"data":data,'image_name': image_name, 'showqr': showqr})



