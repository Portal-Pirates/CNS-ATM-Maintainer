from django.shortcuts import render, redirect
from django.http.response import StreamingHttpResponse,HttpResponse
from core.models import *
from django.contrib import messages
from .forms import *
from datetime import date

def homepage(request):
    return render(request, "index.html")


class Generate_data_feed:
    data_from_qr = ''
    def __init__(self):
        Generate_data_feed.data_from_qr = ''




def redirect_to_scan_qr(request):
    if request.method == "POST":
        resultant_string = request.POST['data']
        Generate_data_feed.data_from_qr = resultant_string
        return redirect('show')
    else:
        form = QRdata()
        return render(request,"scanqr.html",{'form':form})



def show_data(request):
    return render(request,"listviews.html")




class GetModel:
    static_model = None
    danger_data = None
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
            serial_number = str(result_list[3])
            model_number = str(result_list[4])
            equipment_type = str(result_list[5])
            print(equipment_name,airport_name,station_name,serial_number,model_number,equipment_type)
            if Airports.objects.filter(Airport_Location = airport_name).exists():
                if Stations.objects.filter(station_name = station_name).exists():
                    print(serial_number)
                    if Equipments.objects.filter(serial_number = serial_number).exists():
                        some_data= Equipments.objects.filter(serial_number = serial_number)
                        for i in some_data:
                            GetModel.danger_data = i.id
                            break
                        print(GetModel.danger_data)
                        equipment_available = True
                        if equipment_available:
                            try:
                                if equipment_name == "Glid_Path" or equipment_name == ("Glid_Path").upper() or equipment_name == ("Glid_Path").lower() or equipment_name.upper()=="GLID PATH":
                                    self.equipment_model_model = Glid_Path.objects.filter(modal_number = model_number)
                                elif equipment_name == "COMSOFT" or equipment_name == ("COMSOFT").upper() or equipment_name == ("COMSOFT").lower() or equipment_name.upper() == "COMSOFT":
                                    self.equipment_model_model = COMSOFT.objects.filter(modal_number = model_number)
                                elif equipment_name == "VCS_System" or equipment_name == ("VCS_System").upper() or equipment_name == ("VCS_System").lower() or equipment_name.upper() == "VCS SYSTEM":
                                    self.equipment_model_model = VCS_System.objects.filter(modal_number = model_number)
                                elif equipment_name == "Localizer" or equipment_name == ("Localizer").upper() or equipment_name == ("Localizer").lower() or equipment_name.upper() == "LOCALIZER":
                                    self.equipment_model_model = Localizer.objects.filter(modal_number = model_number)
                                elif equipment_name == "DVOR" or equipment_name == ("DVOR").upper() or equipment_name == ("DVOR").lower() or equipment_name.upper() == "DVOR":
                                    self.equipment_model_model = DVOR.objects.filter(modal_number = model_number)
                                elif equipment_name == "NDB" or equipment_name == ("NDB").upper() or equipment_name == ("NDB").lower() or equipment_name.upper() == "NDB":
                                    self.equipment_model_model= NDB.objects.filter(modal_number = model_number)
                                elif equipment_name == "Datis_Terma" or equipment_name == ("Datis_Terma").upper() or equipment_name == ("Datis_Terma").lower() or equipment_name.upper() == "DATIS TERMA":
                                    self.equipment_model_model = Datis_Terma.objects.filter(modal_number = model_number)
                                elif equipment_name == "DVTR" or equipment_name == ("DVTR").upper() or equipment_name == ("DVTR").lower() or equipment_name.upper() == "DVTR":
                                    self.equipment_model_model = DVTR.objects.filter(modal_number = model_number)
                                elif equipment_name == "UPS" or equipment_name == ("UPS").upper() or equipment_name == ("UPS").lower() or equipment_name == "Ups" or equipment_name.upper() == "UPS":
                                    self.equipment_model_model = UPS.objects.filter(modal_number = model_number)
                                else:
                                    try:
                                        self.equipment_model_model = OtherEquipmentsReport.objects.filter(modal_number = model_number)
                                    except Exception:
                                        return("Something went wrong")
                                GetModel.static_model = self.equipment_model_model
                                return self.equipment_model_model
                            except Exception:
                                return("sorry something is wrong")
                    else:
                        return("serial number not exists")
                else:
                    return('Station Not exists')
            else:
                return('Airport Not exists')
        else:
            return("We haven't got your data")






#Function to get model from the date it 
def get_model_from_slug(QuerySet,created):
    try:
        data = QuerySet.get(created = created)
        return data
    except Exception as message:
        return message



#getting models for daily report list view
def dig_models_daily_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,"daily.html")
    else:
        try:
            model = model.filter(report_type = "daily")
            print(model)
            return render(request,"daily.html",{'model':model})
        except Exception:
            messages.success(request,model)
            return render(request,"daily.html")


#Digging models for creating list view for Weekly reports
def dig_models_weekly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    print("I am monthly called model",model)
    if type(model) == str:
        messages.success(request,model)
        return render(request,'weeklyList.html')
    else:
        try:
            print("We are running man")
            model = model.filter(report_type = 'weekly')
            return render(request,"weeklyList.html",{'model':model})
        except Exception:
            messages.success(request,model)
            return render(request,"weeklyList.html")
            

#For Digging detailed information about the selected weekly report
def detail_weekly_report(request,created):
    models = GetModel.static_model
    model3 = GetModel.danger_data
    model_getter = get_model_from_slug(models,created)
    if type(model_getter) == str:
        messages.success(request,"Something went wrong")
        return render(request,"upsWeekly.html")
    else:
        try:
            model2 = models.model.__name__
            print(model2)
            model = model_getter
            print(model3)
            return render(request,"upsWeekly.html",{'models':model,'model2': model2, 'model3':model3})
        except Exception:
            messages.success(request,"Something went wrong")
            return render(request,"upsWeekly.html")


def dig_models_monthly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    model3 = GetModel.danger_data
    if type(model) == str:
        messages.success(request,model)
        return render(request,'UpsMonthly.html')
    else:
        try:
            model2 = model.model.__name__
            print(model2)
            model = model.get(report_type = 'monthly')
            return render(request,"UpsMonthly.html",{'models':model,'model2':model2, 'model3':model3})
        except Exception:
            messages.success(request,"Something went wrong")
            return render(request,"UpsMonthly.html")

def detail_daily_report(request,created):
    models = GetModel.static_model
    model3 = GetModel.danger_data
    model_getter = get_model_from_slug(models,created)
    if type(model_getter) == str:
        messages.success(request,"Something went wrong")
        return render(request,"detailedUps.html")
    else:
        try:
            model2 = models.model.__name__
            print(model2)
            return render(request,"detailedUps.html",{'models':model_getter,'model2':model2,'model3':model3})
        except Exception:
            return render(request,"detailedUps.html")




def dig_models_quaterly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    model3 = GetModel.danger_data
    if type(model) == str:
        messages.success(request,model)
        return render(request,'quaterly.html')
    else:
        try:
            model2 = model.model.__name__
            print(model2)
            model = model.get(report_type = 'quarterly')
            return render(request,"quaterly.html",{'models':model,'model2':model2,'model3':model3})
        except Exception:
            messages.success(request,"Something went wrong while fetching the data")
            return render(request,"quaterly.html")


def dig_models_yearly_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'yearly.html')
    else:
        try:
            model2 = model.model.__name__
            print(model2)
            model3 = GetModel.danger_data
            model = model.get(report_type = 'year')
            return render(request,"yearly.html",{'models':model,'model2':model2,"model3":model3})
        except Exception:
            messages.success(request,"Something went wrong to fetch Yearly report")
            return render(request,"yearly.html")


"""def dig_models_six_month_reports(request):
    model_class = GetModel()
    model = model_class.dig_models_for_results()
    if type(model) == str:
        messages.success(request,model)
        return render(request,'sixmonth.html')
    else:
        try:
            model2 = model.model.__name__
            print(model2)
            model3 = GetModel.danger_data
            model = model.get(report_type = 'halfyearly')
            return render(request,"sixmonth.html",{'models':model,'model2':model2,'model3':model3})
        except Exception:
            messages.success(request,"Something went wrong")
            return render(request,'sixmonth.html')"""


def get_search(model_number,equipment_name):
    print(model_number,equipment_name)
    if equipment_name == "Glid_Path" or equipment_name == ("Glid_Path").upper() or equipment_name == ("Glid_Path").lower() or equipment_name.upper()=="GLID PATH":
        return Glid_Path.objects.filter(modal_number = model_number)
    elif equipment_name == "COMSOFT" or equipment_name == ("COMSOFT").upper() or equipment_name == ("COMSOFT").lower() or equipment_name.upper() == "COMSOFT":
        return COMSOFT.objects.filter(modal_number = model_number)
    elif equipment_name == "VCS_System" or equipment_name == ("VCS_System").upper() or equipment_name == ("VCS_System").lower() or equipment_name.upper() == "VCS SYSTEM":
        return VCS_System.objects.filter(modal_number = model_number)
    elif equipment_name == "Localizer" or equipment_name == ("Localizer").upper() or equipment_name == ("Localizer").lower() or equipment_name.upper() == "LOCALIZER":
        return Localizer.objects.filter(modal_number = model_number)
    elif equipment_name == "DVOR" or equipment_name == ("DVOR").upper() or equipment_name == ("DVOR").lower() or equipment_name.upper() == "DVOR":
        return DVOR.objects.filter(modal_number = model_number)
    elif equipment_name == "NDB" or equipment_name == ("NDB").upper() or equipment_name == ("NDB").lower() or equipment_name.upper() == "NDB":
        return NDB.objects.filter(modal_number = model_number)
    elif equipment_name == "Datis_Terma" or equipment_name == ("Datis_Terma").upper() or equipment_name == ("Datis_Terma").lower() or equipment_name.upper() == "DATIS TERMA":
        return Datis_Terma.objects.filter(modal_number = model_number)
    elif equipment_name == "DVTR" or equipment_name == ("DVTR").upper() or equipment_name == ("DVTR").lower() or equipment_name.upper() == "DVTR":
        return DVTR.objects.filter(modal_number = model_number)
    elif equipment_name == "UPS" or equipment_name == ("UPS").upper() or equipment_name == ("UPS").lower() or equipment_name == "Ups" or equipment_name.upper()=="UPS":
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
        try:
            if report_type == "Daily Report":
                try:
                    check = model[0]
                    model2 = model.model.__name__
                    return render(request,"detailedUps.html",{'models':check,'model2':model2})
                except Exception:
                    messages.success(request,"Sorry We have no data found")
                    return render(request,"detailedUps.html")
            elif report_type == "Weekly Report":
                model2 = model.model.__name__
                print(model2)
                model = model.get(report_type = 'weekly')
                return render(request,"upsWeekly.html",{'models':model,'model2': model2})
            elif report_type == "Monthly Report":
                model2 = model.model.__name__
                print(model2)
                try:
                    model = model.get(report_type = 'monthly')
                    return render(request,"UpsMonthly.html",{'models':model,'model2':model2})
                except Exception:
                    messages.success(request,"No matching Query Found")
                    return render(request,"UpsMonthly.html")
            elif report_type == "Six Month Report":
                messages.success(request,"Something went wrong")
                return render(request,"yearly.html")
                """model2 = model.model.__name__
                print(model2)
                if model2 =='DVOR':
                    model = model.get(report_type = 'halfyearly')
                    return render(request,"sixmonth.html",{'models':model,'model2':model2})
                else:
                    messages.success(request,"we don't have any six month data for you..!!!")
                    return render(request,'sixmonth.html')"""
            elif report_type == "Yearly Report":
                model2 = model.model.__name__
                print(model2)
                try:
                    model = model.get(report_type = 'year')
                    return render(request,"yearly.html",{'models':model,'model2':model2})
                except Exception:
                    messages.success(request,"Sorry We have no data found")
                    return render(request,"yearly.html")
        except Exception:
            messages.success(request,"No report Found for your Query")
            return render(request,"yearly.html")
    else:
        form = SearchForm()
        return render(request,"search.html",{'form':form})



#For getting date difference
def dateDiff(added,removed):
    added_date = date(int(added[0]),int(added[1]),int(added[2]))
    removed_date = date(int(removed[0]),int(removed[1]),int(removed[2]))
    x = removed_date - added_date
    print(x.days,"Is the days difference")
    return x.days


def fault_table_entry_and_prediction(request):
    try:
        if request.method == "POST":
            Equipment_name = request.POST['equipment_name']
            eq_added = request.POST['date_added']
            eq_removed = request.POST['date_removed']
            remarks = request.POST['remarks']
            print(eq_removed,eq_added)
            models = FaultTable()
            models.Equipment_Name = Equipment_name
            models.Date_Added = eq_added
            models.Date_Removed = eq_removed
            models.Remarks = remarks
            added = eq_added.split("-")
            removed = eq_removed.split("-")
            models.duration_it_worked = dateDiff(added,removed)
            models.save() 
            try:
                QuerySet01 = FaultTable.objects.filter(Equipment_Name = Equipment_name)
            except Exception:
                return HttpResponse("There is an issue on your submitted form 😔️😔️😔️")
            sum_of_data= 0 
            number_of_query = 0
            for i in QuerySet01:
                sum_of_data += i.duration_it_worked
                number_of_query += 1
            prediction = sum_of_data//number_of_query
            print("sum of data",sum_of_data)
            print("Number of queries", number_of_query)
            print("I am Prediction", prediction)
            predictmodel = PredictedTable()
            try:
                Queryset_of_eq = PredictedTable.objects.get(Equipment_Name = Equipment_name)
                Queryset_of_eq.prediction = prediction
                Queryset_of_eq.save()
            except Exception:
                predictmodel.Equipment_Name = Equipment_name
                predictmodel.prediction = prediction
                predictmodel.save()
            messages.info(request, "Data saved Successfully :)")
            return render(request, "index.html")
        else:
            form = EquipmentRemoved()
            return render(request,"faultTableEntry.html",{'form':form})
    except Exception:
        form = EquipmentRemoved()
        return render(request,"faultTableEntry.html",{'form':form})
        



    

