from django.shortcuts import render
import json
from django.http import JsonResponse
from core.models import Equipments
# Create your views here.


def NewEntry(request, report_type=None):
    daily = False
    weekly  = False 
    monthly = False
    yearly = False
    if request.method == "GET":
        if report_type == 'Daily':
            daily = True
        elif report_type == 'Weekly':
            weekly = True
        elif report_type == 'Monthly':
            monthly = True
        else:
            yearly = True
        context = {
            'daily': daily,
            'weekly': weekly,
            'monthly': monthly,
            'yearly' : yearly
        }
        return render(request, 'EquipmentnewEntry.html', context)


def select_type(request):
    return render(request, 'Choose.html')


def Equipmentdetail(request, report_type=None):
    equipmentslist = {'GLIDPATH': False, 'COMSOFT': False, 'VCSSYSTEM': False, 'LOCALIZER': False, 'DVOR': False, 'NDB': False, 'DATISTERMA': False, 'DVTR': False, 'UPS': False}
    if request.method == 'POST':
        equipment_name = request.POST['equipment_name']
        serial_number = request.POST['serial_number']
        modal_number = request.POST['modal_number']
        company = request.POST['company']
        equipment_type = request.POST['equipment_type']
        if Equipments.objects.filter(equipment_name=equipment_name).exists():
            temp = equipment_name.split()
            eq_name = ""
            for letter in temp:
                eq_name += letter.upper()
            obj = Equipments.objects.filter(equipment_name=equipment_name)
            context = {
                 eq_name : True,
                 report_type: True,
                 'eqobj': obj
            }
            return render(request, 'newEntry.html', context)
        else:
            temp = equipment_name.split()
            eq_name = ""
            for letter in temp:
                eq_name += letter.upper()
            newobj = Equipments(equipment_name=equipment_name, serial_number=serial_number, modal_number=modal_number, equipment_type=equipment_type, company=company)
            newobj.save()
            context = {
                 eq_name : True,
                 report_type: True,
                'eqobj': newobj
            }
            return render(request, 'newEntry.html', context)



def Equipmentautocomplete(request):
    if 'term' in request.GET:
        qs = Equipments.objects.filter(equipment_name__icontains=request.GET.get('term'))
        equipments = list()
        for item in qs:
            equipments.append(item.equipment_name)
        # titles = [product.title for product in qs]
        return JsonResponse(equipments, safe = False)
    return render(request, "NewEntry.html")