from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse,HttpResponse
from core.camera import *
from core.models import *
from django.contrib import messages
from .forms import *

def homepage(request):
    return render(request, "index.html")

# htao ISE Cz open-cv python and Django saath mill k stream nhi kra paa rhy hai!!!
class Generate_data_feed:
    data_from_qr = ''
    def __init__(self):
        Generate_data_feed.data_from_qr = ''

    """def generate_data(self,camera):
        for i in range(0,1500):
            frame = camera.get_frame()
            try:
                if type(frame) == str:
                    Generate_data_feed.data_from_qr = frame
                    raise StopIteration()
            except StopIteration:
                print("We got your data")
                return HttpResponse("We got your data")
            try:
                yield (b'--frame\r\n'
					    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
            except Exception:
                pass
        else:
            print("Time out")
            return"""

def redirect_to_scan_qr(request):
    if request.method == "POST":
        resultant_string = request.POST['data']
        Generate_data_feed.data_from_qr = resultant_string
        return redirect('show')
    else:
        form = QRdata()
        return render(request,"scanqr.html",{'form':form})

##To be removed##
"""def video_feed(request):
    qr_scanner = Generate_data_feed()
    results = qr_scanner.generate_data(VideoCamera())
    return StreamingHttpResponse(results,content_type='multipart/x-mixed-replace; boundary=frame')"""

def show_data(request):
    return render(request,"listviews.html")

class GetModel:
    static_model = None
    def __init__(self):
        self.equipment_model_model = ""

    def dig_models_for_results(self):
        result_list = Generate_data_feed.data_from_qr
        result_list = result_list.split(",")
        print(result_list)
        if result_list == [''] or result_list==[]:
            return("Blank Received")
        elif result_list!=[''] or result_list!=[]:
            equipment_name = str(result_list[0])
            airport_name = str(result_list[1])
            station_name = str(result_list[2])
            serial_number = int(result_list[3])
            model_number = str(result_list[4])
            equipment_type = str(result_list[5])
            print(equipment_name,airport_name,station_name,serial_number,model_number,equipment_type)
            if Airports.objects.filter(Airport_Name = airport_name).exists():
                if Stations.objects.filter(station_name = station_name).exists():
                    print(serial_number)
                    if Equipments.objects.filter(serial_number = serial_number).exists():
                        equipment_available = True
                        if equipment_available:
                            try:
                                if equipment_name == "Glid_Path" or equipment_name == ("Glid_Path").upper() or equipment_name == ("Glid_Path").lower():
                                    self.equipment_model_model = Glid_Path.objects.filter(modal_number = model_number)
                                elif equipment_name == "COMSOFT" or equipment_name == ("COMSOFT").upper() or equipment_name == ("COMSOFT").lower():
                                    self.equipment_model_model = COMSOFT.objects.filter(modal_number = model_number)
                                elif equipment_name == "VCS_System" or equipment_name == ("VCS_System").upper() or equipment_name == ("VCS_System").lower():
                                    self.equipment_model_model = VCS_System.objects.filter(modal_number = model_number)
                                elif equipment_name == "Localizer" or equipment_name == ("Localizer").upper() or equipment_name == ("Localizer").lower():
                                    self.equipment_model_model = Localizer.objects.filter(modal_number = model_number)
                                elif equipment_name == "DVOR" or equipment_name == ("DVOR").upper() or equipment_name == ("DVOR").lower():
                                    self.equipment_model_model = DVOR.objects.filter(modal_number = model_number)
                                elif equipment_name == "NDB" or equipment_name == ("NDB").upper() or equipment_name == ("NDB").lower():
                                    self.equipment_model_model= NDB.objects.filter(modal_number = model_number)
                                elif equipment_name == "Datis_Terma" or equipment_name == ("Datis_Terma").upper() or equipment_name == ("Datis_Terma").lower():
                                    self.equipment_model_model = Datis_Terma.objects.filter(modal_number = model_number)
                                elif equipment_name == "DVTR" or equipment_name == ("DVTR").upper() or equipment_name == ("DVTR").lower():
                                    self.equipment_model_model = DVTR.objects.filter(modal_number = model_number)
                                elif equipment_name == "UPS" or equipment_name == ("UPS").upper() or equipment_name == ("UPS").lower() or equipment_name == "Ups":
                                    self.equipment_model_model = UPS.objects.filter(modal_number = model_number)
                                else:
                                    self.equipment_model_model = OtherEquipmentsReport.objects.filter(modal_number = model_number)
                                GetModel.static_model = self.equipment_model_model
                                return self.equipment_model_model
                            except Exception:
                                return("sorry something is wrong with QR")
                    else:
                        return("serial number not exists")
                else:
                    return('Station Not exists')
            else:
                return('Airport Not exists')
        else:
            return("We haven't got your data")


def get_model_from_slug(QuerySet,created):
    try:
        data = QuerySet.get(created = created)
        return data
    except Exception as message:
        return message

def dig_models_daily_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,"daily.html")
    else:
        model = model.filter(report_type = "daily")
        print(model)
        return render(request,"daily.html",{'model':model})


def dig_models_weekly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    print("I am monthly called model",model)
    if type(model) == str:
        messages.success(request,model)
        return render(request,'upsWeekly.html')
    else:
        model2 = model.model.__name__
        print(model2)
        model = model.get(report_type = 'weekly')
        return render(request,"upsWeekly.html",{'models':model,'model2': model2})


def dig_models_monthly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'UpsMonthly.html')
    else:
        model2 = model.model.__name__
        print(model2)
        model = model.get(report_type = 'mothly')
        return render(request,"UpsMonthly.html",{'models':model,'model2':model2})


def detail_daily_report(request,created):
    models = GetModel.static_model
    model_getter = get_model_from_slug(models,created)
    if type(model_getter) == str:
        messages.success(request,"Internal server error")
        return render(request,"detailedUps.html")
    else:
        try:
            model2 = models.model.__name__
            print(model2)
            return render(request,"detailedUps.html",{'models':model_getter,'model2':model2})
        except Exception as message:
            #messages.success(request,message)
            return render(request,"detailedUps.html")




def dig_models_quaterly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'quaterly.html')
    else:
        model2 = model.model.__name__
        print(model2)
        model = model.get(report_type = 'quarterly')
        return render(request,"quaterly.html",{'models':model,'model2':model2})


def dig_models_yearly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'yearly.html')
    else:
        model2 = model.model.__name__
        print(model2)
        model = model.get(report_type = 'year')
        return render(request,"yearly.html",{'models':model,'model2':model2})


def dig_models_six_month_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'sixmonth.html')
    else:
        model2 = model.model.__name__
        print(model2)
        if model2 =='DVOR':
            model = model.get(report_type = 'halfyearly')
            return render(request,"sixmonth.html",{'models':model,'model2':model2})
        else:
            messages.success(request,"we don't have any six month data for you..!!!")
            return render(request,'sixmonth.html')


def get_search(model_number,equipment_name):
    print(model_number,equipment_name)
    if equipment_name == "Glid_Path" or equipment_name == ("Glid_Path").upper() or equipment_name == ("Glid_Path").lower():
        return Glid_Path.objects.filter(modal_number = model_number)
    elif equipment_name == "COMSOFT" or equipment_name == ("COMSOFT").upper() or equipment_name == ("COMSOFT").lower():
        return COMSOFT.objects.filter(modal_number = model_number)
    elif equipment_name == "VCS_System" or equipment_name == ("VCS_System").upper() or equipment_name == ("VCS_System").lower():
        return VCS_System.objects.filter(modal_number = model_number)
    elif equipment_name == "Localizer" or equipment_name == ("Localizer").upper() or equipment_name == ("Localizer").lower():
        return Localizer.objects.filter(modal_number = model_number)
    elif equipment_name == "DVOR" or equipment_name == ("DVOR").upper() or equipment_name == ("DVOR").lower():
        return DVOR.objects.filter(modal_number = model_number)
    elif equipment_name == "NDB" or equipment_name == ("NDB").upper() or equipment_name == ("NDB").lower():
        return NDB.objects.filter(modal_number = model_number)
    elif equipment_name == "Datis_Terma" or equipment_name == ("Datis_Terma").upper() or equipment_name == ("Datis_Terma").lower():
        return Datis_Terma.objects.filter(modal_number = model_number)
    elif equipment_name == "DVTR" or equipment_name == ("DVTR").upper() or equipment_name == ("DVTR").lower():
        return DVTR.objects.filter(modal_number = model_number)
    elif equipment_name == "UPS" or equipment_name == ("UPS").upper() or equipment_name == ("UPS").lower() or equipment_name == "Ups":
        return UPS.objects.filter(modal_number = model_number)
    else:
        try:
            return OtherEquipmentsReport.objects.filter(modal_number = model_number)
        except Exception:
            return("No data found!!!")


def search_in_action(request):
    if request.method=="POST":
        model_number = request.POST['model_number']
        equipment_name = request.POST['equipment_name']
        report_type = request.POST['report_type']
        print(report_type)
        model = get_search(model_number,equipment_name)
        if type(model) == str:
            return HttpResponse("No data found")
        if report_type == "Daily Report":
            check = model[0]
            print(check.Input_frequency)
            model2 = model.model.__name__
            return render(request,"detailedUps.html",{'models':check,'model2':model2})
        elif report_type == "Weekly Report":
            model2 = model.model.__name__
            print(model2)
            model = model.get(report_type = 'weekly')
            return render(request,"upsWeekly.html",{'models':model,'model2': model2})
        elif report_type == "Monthly Report":
            model2 = model.model.__name__
            print(model2)
            try:
                model = model.get(report_type = 'mothly')
                return render(request,"UpsMonthly.html",{'models':model,'model2':model2})
            except Exception:
                messages.success(request,"No matching Query Found")
                return render(request,"UpsMonthly.html")
        elif report_type == "Six Month Report":
            model2 = model.model.__name__
            print(model2)
            if model2 =='DVOR':
                model = model.get(report_type = 'halfyearly')
                return render(request,"sixmonth.html",{'models':model,'model2':model2})
            else:
                messages.success(request,"we don't have any six month data for you..!!!")
                return render(request,'sixmonth.html')
        elif report_type == "Yearly Report":
            model2 = model.model.__name__
            print(model2)
            try:
                model = model.get(report_type = 'year')
                return render(request,"yearly.html",{'models':model,'model2':model2})
            except Exception:
                messages.success(request,"Sorry We have no data found")
                return render(request,"yearly.html")
    else:
        form = SearchForm()
        return render(request,"search.html",{'form':form})
