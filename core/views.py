from django.shortcuts import render
from django.http.response import StreamingHttpResponse,HttpResponse
from core.camera import *
from core.models import *
from django.contrib import messages

def homepage(request):
    return render(request, "index.html")
    

class Generate_data_feed:
    data_from_qr = ''
    def __init__(self):
        Generate_data_feed.data_from_qr = ''
    
    def generate_data(self,camera):
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
            return

def redirect_to_scan_qr(request):
    return render(request,"scanqr.html")

def video_feed(request):
    qr_scanner = Generate_data_feed()
    results = qr_scanner.generate_data(VideoCamera())
    return StreamingHttpResponse(results,content_type='multipart/x-mixed-replace; boundary=frame')


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
            updated_by = str(result_list[5])
            equipment_type = str(result_list[6])
            if Airports.objects.filter(Airport_Name = airport_name).exists():
                if Stations.objects.filter(station_name = station_name).exists():
                    print(serial_number)
                    query_sr_no = Equipments.objects.filter(serial_number = serial_number)
                    q = query_sr_no.all()
                    for i in q:
                        id = i.id
                    print(id)
                    equipment_available = Stations.objects.filter(Number_of_equipments = id).exists()
                    if equipment_available:
                        try:
                            if equipment_type == "Glid_Path" or equipment_type == ("Glid_Path").upper() or equipment_type == ("Glid_Path").lower():
                                self.equipment_model_model = Glid_Path.objects.filter(modal_number = model_number)
                            elif equipment_type == "COMSOFT" or equipment_type == ("COMSOFT").upper() or equipment_type == ("COMSOFT").lower():
                                self.equipment_model_model = COMSOFT.objects.filter(modal_number = model_number)
                            elif equipment_type == "VCS_System" or equipment_type == ("VCS_System").upper() or equipment_type == ("VCS_System").lower():
                                self.equipment_model_model = VCS_System.objects.filter(modal_number = model_number)
                            elif equipment_type == "Localizer" or equipment_type == ("Localizer").upper() or equipment_type == ("Localizer").lower():
                                self.equipment_model_model = Localizer.objects.filter(modal_number = model_number)
                            elif equipment_type == "DVOR" or equipment_type == ("DVOR").upper() or equipment_type == ("DVOR").lower():
                                self.equipment_model_model = DVOR.objects.filter(modal_number = model_number)
                            elif equipment_type == "NDB" or equipment_type == ("NDB").upper() or equipment_type == ("NDB").lower():
                                self.equipment_model_model= NDB.objects.filter(modal_number = model_number)
                            elif equipment_type == "Datis_Terma" or equipment_type == ("Datis_Terma").upper() or equipment_type == ("Datis_Terma").lower():
                                self.equipment_model_model = Datis_Terma.objects.filter(modal_number = model_number)
                            elif equipment_type == "DVTR" or equipment_type == ("DVTR").upper() or equipment_type == ("DVTR").lower():
                                self.equipment_model_model = DVTR.objects.filter(modal_number = model_number)
                            elif equipment_type == "UPS" or equipment_type == ("UPS").upper() or equipment_type == ("UPS").lower() or equipment_type == "Ups":
                                self.equipment_model_model = UPS.objects.filter(modal_number = model_number)
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


def get_model_from_slug(QuerySet,slug):
    try:
        data = QuerySet.get(slug = slug)
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
        model = model.latest('id')
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
        model = model.latest('id')
        return render(request,"UpsMonthly.html",{'models':model,'model2':model2})


def detail_daily_report(request,slug):
    models = GetModel.static_model
    model2 = models.model.__name__
    model_getter = get_model_from_slug(models,slug)
    if type(model_getter) == str:
        messages.success(request,"Internal server error")
        return render(request,"detailedUps.html")
    else:
        print(model2)
        return render(request,"detailedUps.html",{'models':model_getter,'model2':model2})

   
    
def dig_models_quaterly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'quaterly.html')
    else:
        model2 = model.model.__name__
        print(model2)
        model = model.latest('id')
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
        model = model.latest('id')
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
            model = model.latest('id')
            return render(request,"sixmonth.html",{'models':model,'model2':model2})
        else:
            messages.success(request,"we don't have any six month data for you..!!!")
            return render(request,'sixmonth.html')