from django.shortcuts import render
import json
from django.http import JsonResponse
from core.models import Equipments


# For equipment Entry form
def EquipmentNewEntry(request, report_type=None):
    if request.method == "GET":
        daily = False
        weekly  = False 
        monthly = False
        yearly = False
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


# for report Typr
def select_type(request):
    return render(request, 'Choose.html')


# after equipment form submission
def Equipmentdetail(request, report_type=None):
    if request.method == 'POST':
        equipment_name = request.POST['equipment_name']
        serial_number = request.POST['serial_number']
        modal_number = request.POST['modal_number']
        company = request.POST['company']
        equipment_type = request.POST['equipment_type']
        equipment_name = equipment_name.upper()
        if Equipments.objects.filter(equipment_name=equipment_name).exists():
            temp = equipment_name.split()
            eq_name = ""
            for letter in temp:
                eq_name += letter.upper()
            obj = Equipments.objects.filter(equipment_name=equipment_name)
            report_type = report_type.upper()
            context = {
                 eq_name : True,
                 report_type: True,
                 'report': report_type,
                 'eqobj': obj
            }
            return render(request, 'Station&Parameter.html', context)
        else:
            temp = equipment_name.split()
            eq_name = ""
            for letter in temp:
                eq_name += letter.upper()
            newobj = Equipments(equipment_name=equipment_name, serial_number=serial_number, modal_number=modal_number, equipment_type=equipment_type, company=company)
            newobj.save()
            report_type = report_type.upper()
            context = {
                 eq_name : True,
                 report_type: True,
                 'report': report_type,
                'eqobj': newobj
            }
            return render(request, 'Station&Parameter.html', context)

# For actual new Entry of Equipment
def NewEntry(request):
    pass



def Equipmentautocomplete(request):
    if 'term' in request.GET:
        qs = Equipments.objects.filter(equipment_name__icontains=request.GET.get('term'))
        equipments = list()
        for item in qs:
            equipments.append(item.equipment_name)
        # titles = [product.title for product in qs]
        return JsonResponse(equipments, safe = False)
    return render(request, "NewEntry.html")