from django.shortcuts import render


from django.shortcuts import render
from qrcode import *



def HomeView(request):
    return render(request,'QRgenration.html')

def on_generate(request):
    if request.method=='POST':
        equip = request.POST['equipment_name']
        ariport =request.POST['airport_name']
        station = request.POST['station_name']
        serial = request.POST['serial_number']
        modal = request.POST['modal_number']
        updated_by = request.POST['updated_by']
        type = request.POST['equipment_type']


        data = equip+","+ariport+","+station+","+serial+","+modal+","+updated_by+","+type
        image_name = type+equip+modal
        qr=make(data)
        qr.save("static_files/media/"+image_name+".png")
    return render(request,"QRgenration.html",{"data":data,'image_name': image_name})



