from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from core.models import *
from django.contrib import messages


# For equipment Entry form
def EquipmentNewEntry(request, report_type=None):
    if request.method == "GET":
        if request.user.is_authenticated:
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
        else:
            return redirect("/") #It should be updated with login Url


# for report Typr
def select_type(request):
    if request.user.is_authenticated:
        return render(request, 'Choose.html')
    else:
        return redirect("/") #It should be updated with login Url



# after equipment form submission
def Equipmentdetail(request, report_type=None):
    if request.method == 'POST':
        equipment_name = request.POST['equipment_name']
        serial_number = request.POST['serial_number']
        modal_number = request.POST['modal_number']
        company = request.POST['company']
        equipment_type = request.POST['equipment_type']
        equipment_name = equipment_name.upper()
        if Equipments.objects.filter(equipment_name__iexact=equipment_name).exists():
            temp = equipment_name.split()
            eq_name = ""
            for letter in temp:
                eq_name += letter.upper()
            obj = Equipments.objects.filter(equipment_name__iexact=equipment_name).first()
            report_type = report_type.upper()
            context = {
                'station' : True,
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
            newobj = Equipments(equipment_name=eq_name, serial_number=serial_number, modal_number=modal_number, equipment_type=equipment_type, company=company)
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
def NewEntry(request, id=None, report_type=None):
    if request.method == 'POST':
        
        user = User.objects.get(username=request.user)
        station_name = request.POST['station_name']
        remarks  = request.POST['remarks'] 
        status  = int(request.POST['status']) 
        temp = station_name.split()
        st_name = ""

        for letter in temp:
            st_name += letter.upper()
        
        region =  request.POST['region']
        location =  request.POST['location']
        eq_obj = Equipments.objects.filter(id=id).first() # Get equipment object Important        
        
        if Stations.objects.filter(station_name__iexact=st_name).exists():

            st_obj = Stations.objects.filter(station_name__iexact=st_name).first() # Get station object Important
            user_profile = Profile.objects.filter(user = user).first() # get Profile object

            # I just need to fetch fields and make a constructor of equipment report and thats it
            if eq_obj.equipment_name.upper() == 'UPS':
                if report_type.upper() == 'DAILY':
                    Input_voltage = int(request.POST['Input_voltage'])
                    Input_frequency = int(request.POST['Input_frequency'])
                    Output_voltage = int(request.POST['Output_voltage'])
                    output_frequency = int(request.POST['output_frequency'])
                    output_load = int(request.POST['output_load'])
                    Battery_bank_volt = int(request.POST['Battery_bank_volt'])
                    Battery_current = int(request.POST['Battery_current'])
                    working = request.POST['working']
                    upsobj = UPS(status=status, working=working, Battery_current=Battery_current, Battery_bank_volt=Battery_bank_volt, output_load=output_load, output_frequency=output_frequency, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower(), Input_voltage=Input_voltage, Input_frequency=Input_frequency, Output_voltage=Output_voltage)
                    upsobj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'WEEKLY':
                    Power_supply_terminal = int(request.POST['Power_supply_terminal'])
                    check_battery_terminal = int(request.POST['check_battery_terminal'])
                    Battery_condition = int(request.POST['Battery_condition'])
                    UPS_condition = int(request.POST['UPS_condition'])
                    UPS_load_percent = int(request.POST['UPS_load_percent'])
                    Neutral_load = int(request.POST['Neutral_load'])
                    Earthing_codition = int(request.POST['Earthing_codition'])
                    upsobj = UPS(status=status, Earthing_codition=Earthing_codition,Neutral_load=Neutral_load, UPS_load_percent=UPS_load_percent, UPS_condition=UPS_condition, Battery_condition=Battery_condition, check_battery_terminal=check_battery_terminal, Power_supply_terminal=Power_supply_terminal,equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    upsobj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Physicaly_clean_check =int(request.POST['Physicaly_clean_check'])
                    Rx_module_status =int(request.POST['Rx_module_status'])
                    Control_Panel_setup  = int(request.POST['Control_Panel_setup'])
                    Physica_check_antenna_cables = int(request.POST['Physica_check_antenna_cables'])
                    DAT_drive_cleaning = int(request.POST['DAT_drive_cleaning'])
                    Netuno_Server_restart = int(request.POST['Netuno_Server_restart'])
                    upsobj = UPS(status=status, Netuno_Server_restart=Netuno_Server_restart, DAT_drive_cleaning=DAT_drive_cleaning, Physica_check_antenna_cables=Physica_check_antenna_cables, Control_Panel_setup=Control_Panel_setup, Rx_module_status=Rx_module_status, Physicaly_clean_check=Physicaly_clean_check, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    upsobj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                upsobj = UPS(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                upsobj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            if eq_obj.equipment_name.upper() == 'COMSOFT':
                if report_type == 'DAILY':
                    General_cleanliness_room = request.POST['General_cleanliness_room']
                    Status_airconditioners = int(request.POST['Status_airconditioners'])
                    status_obstruction_light= int(request.POST['status_obstruction_light'])
                    main_supply_volt= int(request.POST['main_supply_volt'])
                    main_supply_frequency= int(request.POST['main_supply_frequency'])
                    verify_equipment_on_UPS= request.POST['verify_equipment_on_UPS']
                    status_near_monitor= int(request.POST['status_near_monitor'])
                    status_critical_area= int(request.POST['status_critical_area'])
                    remote_status_indication= int(request.POST['remote_status_indication'])
                    comsoft_obj = COMSOFT(status=status,remote_status_indication=remote_status_indication,status_critical_area=status_critical_area,status_near_monitor=status_near_monitor,verify_equipment_on_UPS=verify_equipment_on_UPS,main_supply_frequency=main_supply_frequency,main_supply_volt=main_supply_volt,status_obstruction_light=status_obstruction_light, Status_airconditioners=Status_airconditioners, General_cleanliness_room=General_cleanliness_room, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    comsoft_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Gps_latitude= int(request.POST['Gps_latitude'])
                    GPS_longitude= int(request.POST['GPS_longitude'])
                    Gps_altitude= int(request.POST['Gps_altitude'])
                    general_result= int(request.POST['general_result'])
                    GPS= int(request.POST['GPS'])
                    voltage_sensing= int(request.POST['voltage_sensing'])
                    FPGA= int(request.POST['FPGA'])
                    Reciever= int(request.POST['Reciever'])
                    Cpu_load= int(request.POST['Cpu_load'])
                    Gps_synch=int( request.POST['Gps_synch'])
                    Intermediate_volt= int(request.POST['Intermediate_volt'])
                    Gps_volt= int(request.POST['Gps_volt'])
                    FPGA_volt=int( request.POST['FPGA_volt'])
                    DSP_Board_volt= int(request.POST['DSP_Board_volt'])
                    DSP_board_tmep= int(request.POST['DSP_board_tmep'])
                    Signal_strength_RF_Site=int( request.POST['Signal_strength_RF_Site'])
                    End_to_End_test= int(request.POST['End_to_End_test'])
                    Rx_sensitivity=int( request.POST['Rx_sensitivity'])
                    Test_transmission_loss=int( request.POST['Test_transmission_loss'])
                    Decoder_test= int(request.POST['Decoder_test'])
                    Gnd_station_staus= int(request.POST['Gnd_station_staus'])
                    overall_build_tst_result= int(request.POST['overall_build_tst_result'])
                    UTC_synchr= int(request.POST['UTC_synchr'])
                    comsoft_obj = COMSOFT(status=status,UTC_synchr=UTC_synchr,overall_build_tst_result=overall_build_tst_result,Gnd_station_staus=Gnd_station_staus,Decoder_test=Decoder_test,Test_transmission_loss=Test_transmission_loss,Rx_sensitivity=Rx_sensitivity,End_to_End_test=End_to_End_test,Signal_strength_RF_Site=Signal_strength_RF_Site,DSP_board_tmep=DSP_board_tmep,DSP_Board_volt=DSP_Board_volt,FPGA_volt=FPGA_volt,Gps_volt=Gps_volt,Intermediate_volt=Intermediate_volt,Gps_synch=Gps_synch,Cpu_load=Cpu_load,Reciever=Reciever,FPGA=FPGA,voltage_sensing=voltage_sensing,GPS=GPS,general_result=general_result,Gps_altitude=Gps_altitude,GPS_longitude=GPS_longitude, Gps_latitude=Gps_latitude, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    comsoft_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                comsoft_obj = COMSOFT(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                comsoft_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            if eq_obj.equipment_name.upper() == 'GLIDPATH':
                if report_type.upper() == 'DAILY':
                    General_cleanliness_room = int(request.POST['General_cleanliness_room'])
                    Status_airconditioners = int(request.POST['Status_airconditioners'])
                    status_obstruction_light= int(request.POST['status_obstruction_light'])
                    main_supply_volt= int(request.POST['main_supply_volt'])
                    main_supply_frequency= int(request.POST['main_supply_frequency'])
                    verify_equipment_on_UPS= int(request.POST['verify_equipment_on_UPS'])
                    status_near_monitor= int(request.POST['status_near_monitor'])
                    status_critical_area= int(request.POST['status_critical_area'])
                    remote_status_indication= int(request.POST['remote_status_indication'])
                    #system status indication '' 
                    param= int(request.POST['param'])
                    Disagr= int(request.POST['Disagr'])
                    batt = int( request.POST['batt'])
                    maint= int(request.POST['maint'])
                    standby= int(request.POST['standby'])
                    course=int( request.POST['course'])
                    clearnance=int( request.POST['clearnance'])
                    txtoair=int( request.POST['txtoair'])
                    main=int( request.POST['main'])
                    smps=int( request.POST['smps'])
                    glidpath_obj = Glid_Path(smps=smps,main=main,txtoair=txtoair,clearnance=clearnance,course=course,standby=standby,maint=maint,batt=batt,Disagr=Disagr,param=param,remote_status_indication=remote_status_indication,status_critical_area=status_critical_area,status_near_monitor=status_near_monitor,verify_equipment_on_UPS=verify_equipment_on_UPS,main_supply_frequency=main_supply_frequency,main_supply_volt=main_supply_volt,status_obstruction_light=status_obstruction_light,Status_airconditioners=Status_airconditioners,General_cleanliness_room=General_cleanliness_room,status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                    
                if report_type.upper() == 'WEEKLY':
                    System_time_synch=request.POST['System_time_synch']
                    time_of_observation_UTC=request.POST['time_of_observation_UTC']
                    ILS_datetime_UTC=request.POST['ILS_datetime_UTC']
                    ups_out_volt= int(request.POST['ups_out_volt'])
                    ups_out_freq=int(request.POST['ups_out_freq'])
                    ups_battery_volt=int(request.POST['ups_battery_volt'])
                    battery_volt=int(request.POST['battery_volt'])
                    opearation_on_battery=int(request.POST['opearation_on_battery'])
                    RMS_5volt=int(request.POST['RMS_5volt'])
                    RMS_battery=int(request.POST['RMS_battery'])
                    PS1=int(request.POST['PS1'])
                    PS2=int(request.POST['PS2'])
                    CLR90=int(request.POST['CLR90'])
                    COU150=int(request.POST['COU150'])
                    COU90=int(request.POST['COU90'])
                    glidpath_obj = Glid_Path(COU90=COU90,COU150=COU150,CLR90=CLR90,PS2=PS2,PS1=PS1,RMS_battery=RMS_battery,RMS_5volt=RMS_5volt,opearation_on_battery=opearation_on_battery,battery_volt=battery_volt,ups_battery_volt=ups_battery_volt,ups_out_freq=ups_out_freq,ups_out_volt=ups_out_volt,ILS_datetime_UTC=ILS_datetime_UTC,time_of_observation_UTC=time_of_observation_UTC,System_time_synch=System_time_synch, status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

                if report_type.upper() == 'MONTHLY':
                    Path_augle =int(request.POST['Path_augle'])
                    change_in_displacement_sens =int(request.POST['change_in_displacement_sens'])
                    clearance_signal=int(request.POST['clearance_signal'])
                    reduciton_power=int(request.POST['reduciton_power'])
                    total_time=int(request.POST['total_time'])
                    moitor_sys_oper=int(request.POST['moitor_sys_oper'])
                    all_function_remote=int(request.POST['all_function_remote'])
                    grading_of_critical_are=int(request.POST['grading_of_critical_are'])
                    Envionment=int(request.POST['Envionment'])
                    status_rc_lines=int(request.POST['status_rc_lines'])
                    glidpath_obj = Glid_Path(status_rc_lines=status_rc_lines,Envionment=Envionment,grading_of_critical_are=grading_of_critical_are,all_function_remote=all_function_remote,moitor_sys_oper=moitor_sys_oper,total_time=total_time,reduciton_power=reduciton_power,clearance_signal=clearance_signal,change_in_displacement_sens=change_in_displacement_sens,Path_augle=Path_augle, status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'YEARLY':
                    Frequency = int(request.POST['Frequency '])
                    unwanted_modulation= int(request.POST['unwanted_modulation'])
                    carrier_modulation_freq=int( request.POST['carrier_modulation_freq'])
                    carrier_modulation_homm= int(request.POST['carrier_modulation_homm'])
                    phase_of_modulation_system=int( request.POST['phase_of_modulation_system'])
                    glidpath_obj = Glid_Path(phase_of_modulation_system=phase_of_modulation_system,carrier_modulation_freq=carrier_modulation_freq,unwanted_modulation=unwanted_modulation,Frequency=Frequency,status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

            if eq_obj.equipment_name.upper() == 'VCSSYSTEM':
                if report_type.upper() == 'DAILY':
                    Ac_volt_UPS1= request.POST['Ac_volt_UPS1']
                    Condition_UPS1= request.POST['Condition_UPS1']
                    RAD1PSU= request.POST['RAD1PSU']
                    TEL1_PSU= request.POST['TEL1_PSU']
                    TEL2_PSU= request.POST['TEL2_PSU']
                    TEL3_PSU= request.POST['TEL3_PSU']
                    TEL4_PSU= request.POST['TEL4_PSU']
                    PSU_FuseLED= request.POST['PSU_FuseLED']
                    system_A= request.POST['system_A']
                    Overall_perform= request.POST['Overall_perform']
                    vcs_obj = VCS_System( Overall_perform=Overall_perform,
                                system_A=system_A,
                                PSU_FuseLED=PSU_FuseLED,
                                TEL4_PSU=TEL4_PSU,
                                TEL3_PSU=TEL3_PSU,
                                TEL2_PSU=TEL2_PSU,
                                TEL1_PSU=TEL1_PSU,
                                RAD1PSU=RAD1PSU,
                                Condition_UPS1=Condition_UPS1,
                                Ac_volt_UPS1=Ac_volt_UPS1,
                                status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    vcs_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'WEEKLY':
                    DMC01D5= request.POST['DMC01D5']
                    D2= request.POST['D2']
                    D3= request.POST['D3']
                    D4= request.POST['D4']
                    PDE_4601= request.POST['PDE_4601']
                    DMC02= request.POST['DMC02']
                    PDE4601= request.POST['PDE4601']
                    D5= request.POST['D5']
                    MPC_01= request.POST['MPC_01']
                    D1PDE4662= request.POST['D1PDE4662']
                    vcs_obj =  VCS_System( DMC01D5=DMC01D5,
                                D2=D2,
                                D3=D3,
                                D4=D4,
                                PDE_4601=PDE_4601,
                                DMC02=DMC02,
                                PDE4601=PDE4601,
                                D5=D5,
                                MPC_01=MPC_01,
                                D1PDE4662=D1PDE4662,
                    status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    vcs_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                vcs_obj =  VCS_System(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                vcs_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
                
            if eq_obj.equipment_name.upper() == 'LOCALIZER':
                if report_type.upper() == 'DAILY':
                    General_cleanliness_room = int(request.POST['General_cleanliness_room'])
                    Status_airconditioners = int(request.POST['Status_airconditioners'])
                    status_obstruction_light = int(request.POST['status_obstruction_light'])
                    main_supply_volt = int(request.POST['main_supply_volt'])
                    main_supply_frequency = int(request.POST['main_supply_frequency'])
                    localizer_obj = Localizer(status_obstruction_light=status_obstruction_light,
                                              main_supply_volt=main_supply_volt,
                                              main_supply_frequency=main_supply_frequency,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj, created_by=user_profile,
                        report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'WEEKLY':
                    System_time_synch = int(request.POST['System_time_synch'])
                    Time_of_observ_UTC = int(request.POST['Time_of_observ_UTC'])
                    ILS_data_UTC = int(request.POST['ILS_data_UTC'])
                    Time_source_synch = int(request.POST['Time_source_synch'])
                    Ups_out_volt = int(request.POST['Ups_out_volt'])
                    Ups_out_freq = int(request.POST['Ups_out_freq'])
                    Ups_battery_volt = int(request.POST['Ups_battery_volt'])
                    Battery_volt_before_discharge =int( request.POST['Battery_volt_before_discharge'])
                    operation_on_battery = int(request.POST['operation_on_battery'])
                    Battery_terminal_cleaned = int(request.POST['Battery_terminal_cleaned'])
                    course_LPA = int(request.POST['course_LPA'])
                    CSBlevel =int( request.POST['CSBlevel'])
                    SBOlevel = int(request.POST['SBOlevel'])
                    PH_Corr_peak_lev =int( request.POST['PH_Corr_peak_lev'])
                    CLR_GPA = int(request.POST['CLR_GPA'])
                    course_shift = request.POST['course_shift']
                    change_in_displ_sensitivity = request.POST['change_in_displ_sensitivity']
                    Reduction_pow = request.POST['Reduction_pow']
                    Total_time_out_tolerance = int(request.POST['Total_time_out_tolerance'])
                    physical_inspection =int( request.POST['physical_inspection'])
                    check_allcables_conn = int(request.POST['check_allcables_conn'])
                    check_allnuts_bolt = int(request.POST['check_allnuts_bolt'])
                    Tx_parameters_DC_pow = int(request.POST['Tx_parameters_DC_pow'])
                    MonitorSystemOperation = int(request.POST['MonitorSystemOperation'])
                    All_function_remotecontrol = int(request.POST['All_function_remotecontrol'])
                    Grading_ofcritical_area = int(request.POST['Grading_ofcritical_area'])
                    Environment_vegetaion = int(request.POST['Environment_vegetaion'])
                    status_RClines = int(request.POST['status_RClines'])
                    auto_changeover_value = int(request.POST['auto_changeover_value'])
                    PA27Level = int(request.POST['PA27Level'])
                    Auto_changeOver_ok = int(request.POST['Auto_changeOver_ok'])
                    Auto_shutdown_from_tx = int(request.POST['Auto_shutdown_from_tx'])
                    localizer_obj = Localizer(System_time_synch=System_time_synch,
                                              Time_of_observ_UTC=Time_of_observ_UTC,
                                              Time_source_synch=Time_source_synch,
                                              ILS_data_UTC=ILS_data_UTC,
                                              Ups_battery_volt=Ups_battery_volt,
                                              Ups_out_freq=Ups_out_freq,
                                              Ups_out_volt=Ups_out_volt,
                                              Battery_volt_before_discharge=Battery_volt_before_discharge,
                                              operation_on_battery=operation_on_battery,
                                              Battery_terminal_cleaned=Battery_terminal_cleaned,
                                              course_LPA=course_LPA,
                                              CSBlevel=CSBlevel,
                                              SBOlevel=SBOlevel,
                                              PH_Corr_peak_lev=PH_Corr_peak_lev,
                                              CLR_GPA=CLR_GPA,
                                              Total_time_out_tolerance=Total_time_out_tolerance,
                                              physical_inspection=physical_inspection,
                                              check_allcables_conn=check_allcables_conn,
                                              check_allnuts_bolt=check_allnuts_bolt,
                                              Tx_parameters_DC_pow=Tx_parameters_DC_pow,
                                              MonitorSystemOperation=MonitorSystemOperation,
                                              All_function_remotecontrol=All_function_remotecontrol,
                                              Grading_ofcritical_area=Grading_ofcritical_area,
                                              Environment_vegetaion=Environment_vegetaion,
                                              status_RClines=status_RClines,
                                              auto_changeover_value=auto_changeover_value,
                                              PA27Level=PA27Level,
                                              Auto_changeOver_ok=Auto_changeOver_ok,
                                              Auto_shutdown_from_tx=Auto_shutdown_from_tx,
                                              status=status, equipment_name=eq_obj.equipment_name,
                                              modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                              Airport_Location=location, station_name=st_obj, created_by=user_profile,
                                              report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Equ_rack_earth_resis = int(request.POST['Equ_rack_earth_resis'])
                    Earth_resis_antenna = int(request.POST['Earth_resis_antenna'])
                    Earth_resis_NF_monitor_antenna = int(request.POST['Earth_resis_NF_monitor_antenna'])
                    Earth_resisFFM = int(request.POST['Earth_resisFFM'])
                    Earth_to_neutral_volt = int(request.POST['Earth_to_neutral_volt'])
                    localizer_obj = Localizer(Equ_rack_earth_resis=Equ_rack_earth_resis,
                                              Earth_resis_antenna=Earth_resis_antenna,
                                              Earth_resis_NF_monitor_antenna=Earth_resis_NF_monitor_antenna,
                                              Earth_resisFFM=Earth_resisFFM,
                                              Earth_to_neutral_volt=Earth_to_neutral_volt,
                                              status=status, equipment_name=eq_obj.equipment_name,
                                              modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                              Airport_Location=location, station_name=st_obj, created_by=user_profile,
                                              report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'YEARLY':
                    Suprious_modul = int(request.POST['Suprious_modul'])
                    Coverage_dist = int(request.POST['Coverage_dist'])
                    Carrier_modulation = int(request.POST['Carrier_modulation'])
                    carrier_modul_harmonic = int(request.POST['carrier_modul_harmonic'])
                    Carrier_module_hor_contetn = int(request.POST['Carrier_module_hor_contetn'])
                    sun_modul_depths = int(request.POST['sun_modul_depths'])
                    course_alignment = request.POST['course_alignment']
                    identification = int(request.POST['identification'])
                    identification_repetition_rate = int(request.POST['identification_repetition_rate'])
                    localizer_obj= Localizer(Suprious_modul=Suprious_modul,Coverage_dist=Coverage_dist,Carrier_modulation=Carrier_modulation,Carrier_module_hor_contetn=Carrier_module_hor_contetn,Carrier_module_harmonic=carrier_modul_harmonic,sun_modul_depths=sun_modul_depths,identification=identification,identification_repetition_rate=identification_repetition_rate,status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

            if eq_obj.equipment_name.upper() == 'DVOR':
                if report_type.upper() == 'DAILY':
                    status_air_conditioners = int(request.POST['status_air_conditioners'])
                    shelter_temp_in_celcius = int(request.POST['shelter_temp_in_celcius'])
                    UPS_input_volt_frequency = int(request.POST['UPS_input_volt_frequency'])
                    PS_output_volt_frequency = int(request.POST['PS_output_volt_frequency'])
                    status_battery_operation = int(request.POST['status_battery_operation'])
                    hours_operation = int(request.POST['hours_operation'])
                    Alarm = int(request.POST['Alarm'])

                    Dvor_obj = DVOR(status_air_conditioners=status_air_conditioners,
                                    shelter_temp_in_celcius=shelter_temp_in_celcius,
                                    UPS_input_volt_frequency=UPS_input_volt_frequency,
                                    PS_output_volt_frequency=PS_output_volt_frequency,
                                    status_battery_operation=status_battery_operation,
                                    hours_operation=hours_operation,
                                    Alarm=Alarm,status=status, equipment_name=eq_obj.equipment_name,
                                              modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                              Airport_Location=location, station_name=st_obj,
                                              created_by=user_profile,
                                              report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')


                if report_type.upper() == 'WEEKLY':
                    Carrier_pow = int(request.POST['Carrier_pow'])
                    AM_30hz = int(request.POST['AM_30hz'])
                    Am_1020hz = int(request.POST['Am_1020hz'])
                    USB_level = int(request.POST['USB_level'])
                    USB_RF_Phase = int(request.POST['USB_RF_Phase'])
                    LSB_level = int(request.POST['LSB_level'])
                    Azinmuth = int(request.POST['Azinmuth'])
                    RF_level = int(request.POST['RF_level'])
                    FM_index = int(request.POST['FM_index'])
                    Carrier_frequency = int(request.POST[''])
                    USB_frequency = int(request.POST['Carrier_frequency'])
                    LSB_frequency = int(request.POST['LSB_frequency'])
                    Azimuth_Ul_near = int(request.POST['Azimuth_Ul_near'])
                    Azimuth_LL_nar = int(request.POST['Azimuth_LL_nar'])
                    battery_volt = int(request.POST['battery_volt'])
                    battery_half_volt =int( request.POST['battery_half_volt'])
                    battery_current =int( request.POST['battery_current'])
                    Dvor_obj = DVOR(Carrier_pow=Carrier_pow,
                                    Am_1020hz=Am_1020hz,
                                    AM_30hz=AM_30hz,USB_level=USB_level,
                                    USB_RF_Phase=USB_RF_Phase,
                                    LSB_level=LSB_level,Azinmuth=Azinmuth,
                                    RF_level=RF_level,FM_index=FM_index,
                                    Carrier_frequency=Carrier_frequency,USB_frequency=USB_frequency,
                                    LSB_frequency=LSB_frequency,Azimuth_Ul_near=Azimuth_Ul_near,
                                    Azimuth_LL_nar=Azimuth_LL_nar,battery_volt=battery_volt,
                                    battery_half_volt=battery_half_volt,battery_current=battery_current,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Eq_earth_rack_resistance = int(request.POST['Eq_earth_rack_resistance'])
                    earth_resistance_at_antenna = int(request.POST['earth_resistance_at_antenna'])
                    earth_natural_volt = int(request.POST['earth_natural_volt'])
                    earth_resis_lighting = int(request.POST['earth_resis_lighting'])
                    status_of_lighting_protection_system = int(request.POST['status_of_lighting_protection_system'])
                    status_SPD_at_eq_room = int(request.POST['status_SPD_at_eq_room'])
                    Dvor_obj = DVOR(Eq_earth_rack_resistance=Eq_earth_rack_resistance,
                                    earth_resistance_at_antenna=earth_resistance_at_antenna,
                                    earth_natural_volt=earth_natural_volt,
                                    earth_resis_lighting=earth_resis_lighting,
                                    status_of_lighting_protection_system=status_of_lighting_protection_system,
                                    status_SPD_at_eq_room=status_SPD_at_eq_room,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'YEARLY':
                    Carrier_frequency = int(request.POST['Carrier_frequency'])
                    Hz_derivation = int(request.POST['Hz_derivation'])
                    Hz_modulation_depth = int(request.POST['Hz_modulation_depth'])
                    Hz_modulation_frequency = int(request.POST['Hz_modulation_frequency'])
                    identification_speed = int(request.POST['identification_speed'])
                    identification_repetition = int(request.POST['identification_repetition'])
                    identification_tone_frequency = int(request.POST['identification_tone_frequency'])
                    Bearing_monitor = int(request.POST['Bearing_monitor'])
                    Dvor_obj = DVOR(
                        Carrier_frequency=Carrier_frequency,
                        Hz_derivation=Hz_derivation,
                        Hz_modulation_depth=Hz_modulation_depth,
                        Hz_modulation_frequency=Hz_modulation_frequency,
                        identification_speed=identification_speed,
                        identification_repetition=identification_repetition,
                        identification_tone_frequency=identification_tone_frequency,
                        Bearing_monitor=Bearing_monitor,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
            if eq_obj.equipment_name.upper() == 'NDB':
                if report_type.upper() == 'DAILY':
                    room_temp = int(request.POST['room_temp'])
                    AC_main_volt = int(request.POST['AC_main_volt'])
                    UPS_out_volt = int(request.POST['UPS_out_volt'])
                    reflected_power = int(request.POST['reflected_power'])
                    Forword_Power = int(request.POST['Forword_Power'])
                    modulation = int(request.POST['modulation'])
                    PA_volt = int(request.POST['PA_volt'])
                    PA_current = int(request.POST['PA_current'])
                    System_staus_LED = int(request.POST['System_staus_LED'])
                    primary_tx_led = int(request.POST['primary_tx_led'])
                    tx_power_on_led = int(request.POST['tx_power_on_led'])

                    ndb_obj=NDB(room_temp=room_temp,
                                AC_main_volt=AC_main_volt,
                                UPS_out_volt=UPS_out_volt,
                                reflected_power=reflected_power,
                                Forword_Power=Forword_Power,
                                modulation=modulation,
                                PA_current=PA_current,
                                PA_volt=PA_volt,
                                System_staus_LED=System_staus_LED,
                                primary_tx_led=primary_tx_led,
                                tx_power_on_led=tx_power_on_led,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

                if report_type.upper() == 'WEEKLY':
                    main_pow_supp_terminal = int(request.POST['main_pow_supp_terminal'])
                    check_battery_terminal = int(request.POST['check_battery_terminal'])
                    condition_of_Battery = int(request.POST['condition_of_Battery'])
                    condition_of_UPS = int(request.POST['condition_of_UPS'])
                    UPs_out_load = int(request.POST['UPs_out_load'])
                    condition_earthing = int(request.POST['condition_earthing'])
                    ndb_obj = NDB(main_pow_supp_terminal=main_pow_supp_terminal,
                                  check_battery_terminal=check_battery_terminal,
                                  condition_of_Battery=condition_of_Battery,
                                  condition_of_UPS=condition_of_UPS,
                                  UPs_out_load=UPs_out_load,
                                  condition_earthing=condition_earthing,
                        status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Carry_out_pow_measur = int(request.POST['Carry_out_pow_measur'])
                    depth_modulation = int(request.POST['depth_modulation'])
                    ident_code = int(request.POST['ident_code'])
                    check_antenna = int(request.POST['check_antenna'])
                    check_ACU = int(request.POST['check_ACU'])
                    ndb_obj = NDB(Carry_out_pow_measur=Carry_out_pow_measur,
                                  depth_modulation=depth_modulation,
                                  ident_code=ident_code,
                                  check_antenna=check_antenna,
                                  check_ACU=check_ACU,
                                    status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper=='YEARLY':
                    check_carrier_freq = int(request.POST['check_carrier_freq'])
                    check_modulation_frq = int(request.POST['check_modulation_frq'])
                    check_monitor_alarm = int(request.POST['check_monitor_alarm'])
                    ndb_obj = NDB(check_carrier_freq=check_carrier_freq,
                                  check_modulation_frq=check_modulation_frq,
                                  check_monitor_alarm=check_monitor_alarm,
                                  status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

            if eq_obj.equipment_name.upper() == 'DATISTERMA':
                if report_type.upper() == 'DAILY':
                    ndb_obj = Datis_Terma(status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                d_obj = Datis_Terma(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                d_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            if eq_obj.equipment_name.upper() == 'DVTR':
                if report_type.upper() == 'DAILY':
                    room_temp = int(request.POST['room_temp'])
                    AC_main_volt = int(request.POST['AC_main_volt'])
                    UPS_out_volt = int(request.POST['UPS_out_volt'])
                    cleanlines = int(request.POST['cleanlines']     )
                    status_UPS = int(request.POST['status_UPS'])
                    recording_all_channels =int( request.POST['recording_all_channels'])
                    media_staus = int(request.POST['media_staus'])
                    status_indication = int(request.POST['status_indication'])
                    status_cooling_fans = int(request.POST['status_cooling_fans'])
                    Free_space_disk = int(request.POST['Free_space_disk'])
                    ndb_obj = DVTR(room_temp=room_temp,AC_main_volt=AC_main_volt,
                          UPS_out_volt=UPS_out_volt,cleanlines=cleanlines,
                          status_UPS=status_UPS,
                          recording_all_channels=recording_all_channels,
                          media_staus=media_staus,
                          status_indication=status_indication,
                          status_cooling_fans=status_cooling_fans,
                          Free_space_disk=Free_space_disk,
                          status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    cleaning_PC_dust = int(request.POST['cleaning_PC_dust'])
                    Check_connectors = int(request.POST['Check_connectors'])
                    check_battery_backup = int(request.POST['check_battery_backup'])
                    program_to_Check_HDD = int(request.POST['program_to_Check_HDD'])
                    Application_only_forH24 = int(request.POST['Application_only_forH24'])
                    ndb_obj = DVTR(cleaning_PC_dust=cleaning_PC_dust,
                                  Check_connectors=Check_connectors,
                                  check_battery_backup=check_battery_backup,
                                  program_to_Check_HDD=program_to_Check_HDD,
                                  Application_only_forH24=Application_only_forH24,
                                status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                ndb_obj = DVTR(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                ndb_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            otherEq_obj = OtherEquipmentsReport(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
            otherEq_obj.save()
            messages.success(request, "Saved Successfully...")
            return redirect('/')
              


        
        
        
        else:

            location_obj = Airports.objects.filter(Airport_Location__iexact=location.upper()).first()
            st_obj = Stations(station_name=st_name, region=region, location=location_obj)
            st_obj.save()
            user_profile = Profile.objects.filter(user = user).first() # get Profile object

            # I just need to fetch fields and make a constructor of equipment report and thats it
            if eq_obj.equipment_name.upper() == 'UPS':
                if report_type.upper() == 'DAILY':
                    Input_voltage = int(request.POST['Input_voltage'])
                    Input_frequency = int(request.POST['Input_frequency'])
                    Output_voltage = int(request.POST['Output_voltage'])
                    output_frequency = int(request.POST['output_frequency'])
                    output_load = int(request.POST['output_load'])
                    Battery_bank_volt = int(request.POST['Battery_bank_volt'])
                    Battery_current = int(request.POST['Battery_current'])
                    working = request.POST['working']
                    upsobj = UPS(status=status, working=working, Battery_current=Battery_current, Battery_bank_volt=Battery_bank_volt, output_load=output_load, output_frequency=output_frequency, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower(), Input_voltage=Input_voltage, Input_frequency=Input_frequency, Output_voltage=Output_voltage)
                    upsobj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'WEEKLY':
                    Power_supply_terminal = int(request.POST['Power_supply_terminal'])
                    check_battery_terminal = int(request.POST['check_battery_terminal'])
                    Battery_condition = int(request.POST['Battery_condition'])
                    UPS_condition = int(request.POST['UPS_condition'])
                    UPS_load_percent = int(request.POST['UPS_load_percent'])
                    Neutral_load = int(request.POST['Neutral_load'])
                    Earthing_codition = int(request.POST['Earthing_codition'])
                    upsobj = UPS(status=status, Earthing_codition=Earthing_codition,Neutral_load=Neutral_load, UPS_load_percent=UPS_load_percent, UPS_condition=UPS_condition, Battery_condition=Battery_condition, check_battery_terminal=check_battery_terminal, Power_supply_terminal=Power_supply_terminal,equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    upsobj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Physicaly_clean_check =int(request.POST['Physicaly_clean_check'])
                    Rx_module_status =int(request.POST['Rx_module_status'])
                    Control_Panel_setup  = int(request.POST['Control_Panel_setup'])
                    Physica_check_antenna_cables = int(request.POST['Physica_check_antenna_cables'])
                    DAT_drive_cleaning = int(request.POST['DAT_drive_cleaning'])
                    Netuno_Server_restart = int(request.POST['Netuno_Server_restart'])
                    upsobj = UPS(status=status, Netuno_Server_restart=Netuno_Server_restart, DAT_drive_cleaning=DAT_drive_cleaning, Physica_check_antenna_cables=Physica_check_antenna_cables, Control_Panel_setup=Control_Panel_setup, Rx_module_status=Rx_module_status, Physicaly_clean_check=Physicaly_clean_check, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    upsobj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                upsobj = UPS(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                upsobj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            if eq_obj.equipment_name.upper() == 'COMSOFT':
                if report_type == 'DAILY':
                    General_cleanliness_room = request.POST['General_cleanliness_room']
                    Status_airconditioners = int(request.POST['Status_airconditioners'])
                    status_obstruction_light= int(request.POST['status_obstruction_light'])
                    main_supply_volt= int(request.POST['main_supply_volt'])
                    main_supply_frequency= int(request.POST['main_supply_frequency'])
                    verify_equipment_on_UPS= request.POST['verify_equipment_on_UPS']
                    status_near_monitor= int(request.POST['status_near_monitor'])
                    status_critical_area= int(request.POST['status_critical_area'])
                    remote_status_indication= int(request.POST['remote_status_indication'])
                    comsoft_obj = COMSOFT(status=status,remote_status_indication=remote_status_indication,status_critical_area=status_critical_area,status_near_monitor=status_near_monitor,verify_equipment_on_UPS=verify_equipment_on_UPS,main_supply_frequency=main_supply_frequency,main_supply_volt=main_supply_volt,status_obstruction_light=status_obstruction_light, Status_airconditioners=Status_airconditioners, General_cleanliness_room=General_cleanliness_room, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    comsoft_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Gps_latitude= int(request.POST['Gps_latitude'])
                    GPS_longitude= int(request.POST['GPS_longitude'])
                    Gps_altitude= int(request.POST['Gps_altitude'])
                    general_result= int(request.POST['general_result'])
                    GPS= int(request.POST['GPS'])
                    voltage_sensing= int(request.POST['voltage_sensing'])
                    FPGA= int(request.POST['FPGA'])
                    Reciever= int(request.POST['Reciever'])
                    Cpu_load= int(request.POST['Cpu_load'])
                    Gps_synch=int( request.POST['Gps_synch'])
                    Intermediate_volt= int(request.POST['Intermediate_volt'])
                    Gps_volt= int(request.POST['Gps_volt'])
                    FPGA_volt=int( request.POST['FPGA_volt'])
                    DSP_Board_volt= int(request.POST['DSP_Board_volt'])
                    DSP_board_tmep= int(request.POST['DSP_board_tmep'])
                    Signal_strength_RF_Site=int( request.POST['Signal_strength_RF_Site'])
                    End_to_End_test= int(request.POST['End_to_End_test'])
                    Rx_sensitivity=int( request.POST['Rx_sensitivity'])
                    Test_transmission_loss=int( request.POST['Test_transmission_loss'])
                    Decoder_test= int(request.POST['Decoder_test'])
                    Gnd_station_staus= int(request.POST['Gnd_station_staus'])
                    overall_build_tst_result= int(request.POST['overall_build_tst_result'])
                    UTC_synchr= int(request.POST['UTC_synchr'])
                    comsoft_obj = COMSOFT(status=status,UTC_synchr=UTC_synchr,overall_build_tst_result=overall_build_tst_result,Gnd_station_staus=Gnd_station_staus,Decoder_test=Decoder_test,Test_transmission_loss=Test_transmission_loss,Rx_sensitivity=Rx_sensitivity,End_to_End_test=End_to_End_test,Signal_strength_RF_Site=Signal_strength_RF_Site,DSP_board_tmep=DSP_board_tmep,DSP_Board_volt=DSP_Board_volt,FPGA_volt=FPGA_volt,Gps_volt=Gps_volt,Intermediate_volt=Intermediate_volt,Gps_synch=Gps_synch,Cpu_load=Cpu_load,Reciever=Reciever,FPGA=FPGA,voltage_sensing=voltage_sensing,GPS=GPS,general_result=general_result,Gps_altitude=Gps_altitude,GPS_longitude=GPS_longitude, Gps_latitude=Gps_latitude, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    comsoft_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                comsoft_obj = COMSOFT(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                comsoft_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            if eq_obj.equipment_name.upper() == 'GLIDPATH':
                if report_type.upper() == 'DAILY':
                    General_cleanliness_room = int(request.POST['General_cleanliness_room'])
                    Status_airconditioners = int(request.POST['Status_airconditioners'])
                    status_obstruction_light= int(request.POST['status_obstruction_light'])
                    main_supply_volt= int(request.POST['main_supply_volt'])
                    main_supply_frequency= int(request.POST['main_supply_frequency'])
                    verify_equipment_on_UPS= int(request.POST['verify_equipment_on_UPS'])
                    status_near_monitor= int(request.POST['status_near_monitor'])
                    status_critical_area= int(request.POST['status_critical_area'])
                    remote_status_indication= int(request.POST['remote_status_indication'])
                    #system status indication '' 
                    param= int(request.POST['param'])
                    Disagr= int(request.POST['Disagr'])
                    batt = int( request.POST['batt'])
                    maint= int(request.POST['maint'])
                    standby= int(request.POST['standby'])
                    course=int( request.POST['course'])
                    clearnance=int( request.POST['clearnance'])
                    txtoair=int( request.POST['txtoair'])
                    main=int( request.POST['main'])
                    smps=int( request.POST['smps'])
                    glidpath_obj = Glid_Path(smps=smps,main=main,txtoair=txtoair,clearnance=clearnance,course=course,standby=standby,maint=maint,batt=batt,Disagr=Disagr,param=param,remote_status_indication=remote_status_indication,status_critical_area=status_critical_area,status_near_monitor=status_near_monitor,verify_equipment_on_UPS=verify_equipment_on_UPS,main_supply_frequency=main_supply_frequency,main_supply_volt=main_supply_volt,status_obstruction_light=status_obstruction_light,Status_airconditioners=Status_airconditioners,General_cleanliness_room=General_cleanliness_room,status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                    
                if report_type.upper() == 'WEEKLY':
                    System_time_synch=request.POST['System_time_synch']
                    time_of_observation_UTC=request.POST['time_of_observation_UTC']
                    ILS_datetime_UTC=request.POST['ILS_datetime_UTC']
                    ups_out_volt= int(request.POST['ups_out_volt'])
                    ups_out_freq=int(request.POST['ups_out_freq'])
                    ups_battery_volt=int(request.POST['ups_battery_volt'])
                    battery_volt=int(request.POST['battery_volt'])
                    opearation_on_battery=int(request.POST['opearation_on_battery'])
                    RMS_5volt=int(request.POST['RMS_5volt'])
                    RMS_battery=int(request.POST['RMS_battery'])
                    PS1=int(request.POST['PS1'])
                    PS2=int(request.POST['PS2'])
                    CLR90=int(request.POST['CLR90'])
                    COU150=int(request.POST['COU150'])
                    COU90=int(request.POST['COU90'])
                    glidpath_obj = Glid_Path(COU90=COU90,COU150=COU150,CLR90=CLR90,PS2=PS2,PS1=PS1,RMS_battery=RMS_battery,RMS_5volt=RMS_5volt,opearation_on_battery=opearation_on_battery,battery_volt=battery_volt,ups_battery_volt=ups_battery_volt,ups_out_freq=ups_out_freq,ups_out_volt=ups_out_volt,ILS_datetime_UTC=ILS_datetime_UTC,time_of_observation_UTC=time_of_observation_UTC,System_time_synch=System_time_synch, status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

                if report_type.upper() == 'MONTHLY':
                    Path_augle =int(request.POST['Path_augle'])
                    change_in_displacement_sens =int(request.POST['change_in_displacement_sens'])
                    clearance_signal=int(request.POST['clearance_signal'])
                    reduciton_power=int(request.POST['reduciton_power'])
                    total_time=int(request.POST['total_time'])
                    moitor_sys_oper=int(request.POST['moitor_sys_oper'])
                    all_function_remote=int(request.POST['all_function_remote'])
                    grading_of_critical_are=int(request.POST['grading_of_critical_are'])
                    Envionment=int(request.POST['Envionment'])
                    status_rc_lines=int(request.POST['status_rc_lines'])
                    glidpath_obj = Glid_Path(status_rc_lines=status_rc_lines,Envionment=Envionment,grading_of_critical_are=grading_of_critical_are,all_function_remote=all_function_remote,moitor_sys_oper=moitor_sys_oper,total_time=total_time,reduciton_power=reduciton_power,clearance_signal=clearance_signal,change_in_displacement_sens=change_in_displacement_sens,Path_augle=Path_augle, status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'YEARLY':
                    Frequency = int(request.POST['Frequency '])
                    unwanted_modulation= int(request.POST['unwanted_modulation'])
                    carrier_modulation_freq=int( request.POST['carrier_modulation_freq'])
                    carrier_modulation_homm= int(request.POST['carrier_modulation_homm'])
                    phase_of_modulation_system=int( request.POST['phase_of_modulation_system'])
                    glidpath_obj = Glid_Path(phase_of_modulation_system=phase_of_modulation_system,carrier_modulation_freq=carrier_modulation_freq,unwanted_modulation=unwanted_modulation,Frequency=Frequency,status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    glidpath_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

            if eq_obj.equipment_name.upper() == 'VCSSYSTEM':
                if report_type.upper() == 'DAILY':
                    Ac_volt_UPS1= request.POST['Ac_volt_UPS1']
                    Condition_UPS1= request.POST['Condition_UPS1']
                    RAD1PSU= request.POST['RAD1PSU']
                    TEL1_PSU= request.POST['TEL1_PSU']
                    TEL2_PSU= request.POST['TEL2_PSU']
                    TEL3_PSU= request.POST['TEL3_PSU']
                    TEL4_PSU= request.POST['TEL4_PSU']
                    PSU_FuseLED= request.POST['PSU_FuseLED']
                    system_A= request.POST['system_A']
                    Overall_perform= request.POST['Overall_perform']
                    vcs_obj = VCS_System( Overall_perform=Overall_perform,
                                system_A=system_A,
                                PSU_FuseLED=PSU_FuseLED,
                                TEL4_PSU=TEL4_PSU,
                                TEL3_PSU=TEL3_PSU,
                                TEL2_PSU=TEL2_PSU,
                                TEL1_PSU=TEL1_PSU,
                                RAD1PSU=RAD1PSU,
                                Condition_UPS1=Condition_UPS1,
                                Ac_volt_UPS1=Ac_volt_UPS1,
                                status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    vcs_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'WEEKLY':
                    DMC01D5= request.POST['DMC01D5']
                    D2= request.POST['D2']
                    D3= request.POST['D3']
                    D4= request.POST['D4']
                    PDE_4601= request.POST['PDE_4601']
                    DMC02= request.POST['DMC02']
                    PDE4601= request.POST['PDE4601']
                    D5= request.POST['D5']
                    MPC_01= request.POST['MPC_01']
                    D1PDE4662= request.POST['D1PDE4662']
                    vcs_obj =  VCS_System( DMC01D5=DMC01D5,
                                D2=D2,
                                D3=D3,
                                D4=D4,
                                PDE_4601=PDE_4601,
                                DMC02=DMC02,
                                PDE4601=PDE4601,
                                D5=D5,
                                MPC_01=MPC_01,
                                D1PDE4662=D1PDE4662,
                    status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    vcs_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                vcs_obj =  VCS_System(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                vcs_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
                
            if eq_obj.equipment_name.upper() == 'LOCALIZER':
                if report_type.upper() == 'DAILY':
                    General_cleanliness_room = int(request.POST['General_cleanliness_room'])
                    Status_airconditioners = int(request.POST['Status_airconditioners'])
                    status_obstruction_light = int(request.POST['status_obstruction_light'])
                    main_supply_volt = int(request.POST['main_supply_volt'])
                    main_supply_frequency = int(request.POST['main_supply_frequency'])
                    localizer_obj = Localizer(status_obstruction_light=status_obstruction_light,
                                              main_supply_volt=main_supply_volt,
                                              main_supply_frequency=main_supply_frequency,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj, created_by=user_profile,
                        report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'WEEKLY':
                    System_time_synch = int(request.POST['System_time_synch'])
                    Time_of_observ_UTC = int(request.POST['Time_of_observ_UTC'])
                    ILS_data_UTC = int(request.POST['ILS_data_UTC'])
                    Time_source_synch = int(request.POST['Time_source_synch'])
                    Ups_out_volt = int(request.POST['Ups_out_volt'])
                    Ups_out_freq = int(request.POST['Ups_out_freq'])
                    Ups_battery_volt = int(request.POST['Ups_battery_volt'])
                    Battery_volt_before_discharge =int( request.POST['Battery_volt_before_discharge'])
                    operation_on_battery = int(request.POST['operation_on_battery'])
                    Battery_terminal_cleaned = int(request.POST['Battery_terminal_cleaned'])
                    course_LPA = int(request.POST['course_LPA'])
                    CSBlevel =int( request.POST['CSBlevel'])
                    SBOlevel = int(request.POST['SBOlevel'])
                    PH_Corr_peak_lev =int( request.POST['PH_Corr_peak_lev'])
                    CLR_GPA = int(request.POST['CLR_GPA'])
                    course_shift = request.POST['course_shift']
                    change_in_displ_sensitivity = request.POST['change_in_displ_sensitivity']
                    Reduction_pow = request.POST['Reduction_pow']
                    Total_time_out_tolerance = int(request.POST['Total_time_out_tolerance'])
                    physical_inspection =int( request.POST['physical_inspection'])
                    check_allcables_conn = int(request.POST['check_allcables_conn'])
                    check_allnuts_bolt = int(request.POST['check_allnuts_bolt'])
                    Tx_parameters_DC_pow = int(request.POST['Tx_parameters_DC_pow'])
                    MonitorSystemOperation = int(request.POST['MonitorSystemOperation'])
                    All_function_remotecontrol = int(request.POST['All_function_remotecontrol'])
                    Grading_ofcritical_area = int(request.POST['Grading_ofcritical_area'])
                    Environment_vegetaion = int(request.POST['Environment_vegetaion'])
                    status_RClines = int(request.POST['status_RClines'])
                    auto_changeover_value = int(request.POST['auto_changeover_value'])
                    PA27Level = int(request.POST['PA27Level'])
                    Auto_changeOver_ok = int(request.POST['Auto_changeOver_ok'])
                    Auto_shutdown_from_tx = int(request.POST['Auto_shutdown_from_tx'])
                    localizer_obj = Localizer(System_time_synch=System_time_synch,
                                              Time_of_observ_UTC=Time_of_observ_UTC,
                                              Time_source_synch=Time_source_synch,
                                              ILS_data_UTC=ILS_data_UTC,
                                              Ups_battery_volt=Ups_battery_volt,
                                              Ups_out_freq=Ups_out_freq,
                                              Ups_out_volt=Ups_out_volt,
                                              Battery_volt_before_discharge=Battery_volt_before_discharge,
                                              operation_on_battery=operation_on_battery,
                                              Battery_terminal_cleaned=Battery_terminal_cleaned,
                                              course_LPA=course_LPA,
                                              CSBlevel=CSBlevel,
                                              SBOlevel=SBOlevel,
                                              PH_Corr_peak_lev=PH_Corr_peak_lev,
                                              CLR_GPA=CLR_GPA,
                                              Total_time_out_tolerance=Total_time_out_tolerance,
                                              physical_inspection=physical_inspection,
                                              check_allcables_conn=check_allcables_conn,
                                              check_allnuts_bolt=check_allnuts_bolt,
                                              Tx_parameters_DC_pow=Tx_parameters_DC_pow,
                                              MonitorSystemOperation=MonitorSystemOperation,
                                              All_function_remotecontrol=All_function_remotecontrol,
                                              Grading_ofcritical_area=Grading_ofcritical_area,
                                              Environment_vegetaion=Environment_vegetaion,
                                              status_RClines=status_RClines,
                                              auto_changeover_value=auto_changeover_value,
                                              PA27Level=PA27Level,
                                              Auto_changeOver_ok=Auto_changeOver_ok,
                                              Auto_shutdown_from_tx=Auto_shutdown_from_tx,
                                              status=status, equipment_name=eq_obj.equipment_name,
                                              modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                              Airport_Location=location, station_name=st_obj, created_by=user_profile,
                                              report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Equ_rack_earth_resis = int(request.POST['Equ_rack_earth_resis'])
                    Earth_resis_antenna = int(request.POST['Earth_resis_antenna'])
                    Earth_resis_NF_monitor_antenna = int(request.POST['Earth_resis_NF_monitor_antenna'])
                    Earth_resisFFM = int(request.POST['Earth_resisFFM'])
                    Earth_to_neutral_volt = int(request.POST['Earth_to_neutral_volt'])
                    localizer_obj = Localizer(Equ_rack_earth_resis=Equ_rack_earth_resis,
                                              Earth_resis_antenna=Earth_resis_antenna,
                                              Earth_resis_NF_monitor_antenna=Earth_resis_NF_monitor_antenna,
                                              Earth_resisFFM=Earth_resisFFM,
                                              Earth_to_neutral_volt=Earth_to_neutral_volt,
                                              status=status, equipment_name=eq_obj.equipment_name,
                                              modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                              Airport_Location=location, station_name=st_obj, created_by=user_profile,
                                              report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'YEARLY':
                    Suprious_modul = int(request.POST['Suprious_modul'])
                    Coverage_dist = int(request.POST['Coverage_dist'])
                    Carrier_modulation = int(request.POST['Carrier_modulation'])
                    carrier_modul_harmonic = int(request.POST['carrier_modul_harmonic'])
                    Carrier_module_hor_contetn = int(request.POST['Carrier_module_hor_contetn'])
                    sun_modul_depths = int(request.POST['sun_modul_depths'])
                    course_alignment = request.POST['course_alignment']
                    identification = int(request.POST['identification'])
                    identification_repetition_rate = int(request.POST['identification_repetition_rate'])
                    localizer_obj= Localizer(Suprious_modul=Suprious_modul,Coverage_dist=Coverage_dist,Carrier_modulation=Carrier_modulation,Carrier_module_hor_contetn=Carrier_module_hor_contetn,Carrier_module_harmonic=carrier_modul_harmonic,sun_modul_depths=sun_modul_depths,identification=identification,identification_repetition_rate=identification_repetition_rate,status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                    localizer_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

            if eq_obj.equipment_name.upper() == 'DVOR':
                if report_type.upper() == 'DAILY':
                    status_air_conditioners = int(request.POST['status_air_conditioners'])
                    shelter_temp_in_celcius = int(request.POST['shelter_temp_in_celcius'])
                    UPS_input_volt_frequency = int(request.POST['UPS_input_volt_frequency'])
                    PS_output_volt_frequency = int(request.POST['PS_output_volt_frequency'])
                    status_battery_operation = int(request.POST['status_battery_operation'])
                    hours_operation = int(request.POST['hours_operation'])
                    Alarm = int(request.POST['Alarm'])

                    Dvor_obj = DVOR(status_air_conditioners=status_air_conditioners,
                                    shelter_temp_in_celcius=shelter_temp_in_celcius,
                                    UPS_input_volt_frequency=UPS_input_volt_frequency,
                                    PS_output_volt_frequency=PS_output_volt_frequency,
                                    status_battery_operation=status_battery_operation,
                                    hours_operation=hours_operation,
                                    Alarm=Alarm,status=status, equipment_name=eq_obj.equipment_name,
                                              modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                              Airport_Location=location, station_name=st_obj,
                                              created_by=user_profile,
                                              report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')


                if report_type.upper() == 'WEEKLY':
                    Carrier_pow = int(request.POST['Carrier_pow'])
                    AM_30hz = int(request.POST['AM_30hz'])
                    Am_1020hz = int(request.POST['Am_1020hz'])
                    USB_level = int(request.POST['USB_level'])
                    USB_RF_Phase = int(request.POST['USB_RF_Phase'])
                    LSB_level = int(request.POST['LSB_level'])
                    Azinmuth = int(request.POST['Azinmuth'])
                    RF_level = int(request.POST['RF_level'])
                    FM_index = int(request.POST['FM_index'])
                    Carrier_frequency = int(request.POST[''])
                    USB_frequency = int(request.POST['Carrier_frequency'])
                    LSB_frequency = int(request.POST['LSB_frequency'])
                    Azimuth_Ul_near = int(request.POST['Azimuth_Ul_near'])
                    Azimuth_LL_nar = int(request.POST['Azimuth_LL_nar'])
                    battery_volt = int(request.POST['battery_volt'])
                    battery_half_volt =int( request.POST['battery_half_volt'])
                    battery_current =int( request.POST['battery_current'])
                    Dvor_obj = DVOR(Carrier_pow=Carrier_pow,
                                    Am_1020hz=Am_1020hz,
                                    AM_30hz=AM_30hz,USB_level=USB_level,
                                    USB_RF_Phase=USB_RF_Phase,
                                    LSB_level=LSB_level,Azinmuth=Azinmuth,
                                    RF_level=RF_level,FM_index=FM_index,
                                    Carrier_frequency=Carrier_frequency,USB_frequency=USB_frequency,
                                    LSB_frequency=LSB_frequency,Azimuth_Ul_near=Azimuth_Ul_near,
                                    Azimuth_LL_nar=Azimuth_LL_nar,battery_volt=battery_volt,
                                    battery_half_volt=battery_half_volt,battery_current=battery_current,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Eq_earth_rack_resistance = int(request.POST['Eq_earth_rack_resistance'])
                    earth_resistance_at_antenna = int(request.POST['earth_resistance_at_antenna'])
                    earth_natural_volt = int(request.POST['earth_natural_volt'])
                    earth_resis_lighting = int(request.POST['earth_resis_lighting'])
                    status_of_lighting_protection_system = int(request.POST['status_of_lighting_protection_system'])
                    status_SPD_at_eq_room = int(request.POST['status_SPD_at_eq_room'])
                    Dvor_obj = DVOR(Eq_earth_rack_resistance=Eq_earth_rack_resistance,
                                    earth_resistance_at_antenna=earth_resistance_at_antenna,
                                    earth_natural_volt=earth_natural_volt,
                                    earth_resis_lighting=earth_resis_lighting,
                                    status_of_lighting_protection_system=status_of_lighting_protection_system,
                                    status_SPD_at_eq_room=status_SPD_at_eq_room,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'YEARLY':
                    Carrier_frequency = int(request.POST['Carrier_frequency'])
                    Hz_derivation = int(request.POST['Hz_derivation'])
                    Hz_modulation_depth = int(request.POST['Hz_modulation_depth'])
                    Hz_modulation_frequency = int(request.POST['Hz_modulation_frequency'])
                    identification_speed = int(request.POST['identification_speed'])
                    identification_repetition = int(request.POST['identification_repetition'])
                    identification_tone_frequency = int(request.POST['identification_tone_frequency'])
                    Bearing_monitor = int(request.POST['Bearing_monitor'])
                    Dvor_obj = DVOR(
                        Carrier_frequency=Carrier_frequency,
                        Hz_derivation=Hz_derivation,
                        Hz_modulation_depth=Hz_modulation_depth,
                        Hz_modulation_frequency=Hz_modulation_frequency,
                        identification_speed=identification_speed,
                        identification_repetition=identification_repetition,
                        identification_tone_frequency=identification_tone_frequency,
                        Bearing_monitor=Bearing_monitor,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    Dvor_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
            if eq_obj.equipment_name.upper() == 'NDB':
                if report_type.upper() == 'DAILY':
                    room_temp = int(request.POST['room_temp'])
                    AC_main_volt = int(request.POST['AC_main_volt'])
                    UPS_out_volt = int(request.POST['UPS_out_volt'])
                    reflected_power = int(request.POST['reflected_power'])
                    Forword_Power = int(request.POST['Forword_Power'])
                    modulation = int(request.POST['modulation'])
                    PA_volt = int(request.POST['PA_volt'])
                    PA_current = int(request.POST['PA_current'])
                    System_staus_LED = int(request.POST['System_staus_LED'])
                    primary_tx_led = int(request.POST['primary_tx_led'])
                    tx_power_on_led = int(request.POST['tx_power_on_led'])

                    ndb_obj=NDB(room_temp=room_temp,
                                AC_main_volt=AC_main_volt,
                                UPS_out_volt=UPS_out_volt,
                                reflected_power=reflected_power,
                                Forword_Power=Forword_Power,
                                modulation=modulation,
                                PA_current=PA_current,
                                PA_volt=PA_volt,
                                System_staus_LED=System_staus_LED,
                                primary_tx_led=primary_tx_led,
                                tx_power_on_led=tx_power_on_led,
                        status=status, equipment_name=eq_obj.equipment_name,
                        modal_number=eq_obj.modal_number, Make=eq_obj.company,
                        Airport_Location=location, station_name=st_obj,
                        created_by=user_profile,
                        report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

                if report_type.upper() == 'WEEKLY':
                    main_pow_supp_terminal = int(request.POST['main_pow_supp_terminal'])
                    check_battery_terminal = int(request.POST['check_battery_terminal'])
                    condition_of_Battery = int(request.POST['condition_of_Battery'])
                    condition_of_UPS = int(request.POST['condition_of_UPS'])
                    UPs_out_load = int(request.POST['UPs_out_load'])
                    condition_earthing = int(request.POST['condition_earthing'])
                    ndb_obj = NDB(main_pow_supp_terminal=main_pow_supp_terminal,
                                  check_battery_terminal=check_battery_terminal,
                                  condition_of_Battery=condition_of_Battery,
                                  condition_of_UPS=condition_of_UPS,
                                  UPs_out_load=UPs_out_load,
                                  condition_earthing=condition_earthing,
                        status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    Carry_out_pow_measur = int(request.POST['Carry_out_pow_measur'])
                    depth_modulation = int(request.POST['depth_modulation'])
                    ident_code = int(request.POST['ident_code'])
                    check_antenna = int(request.POST['check_antenna'])
                    check_ACU = int(request.POST['check_ACU'])
                    ndb_obj = NDB(Carry_out_pow_measur=Carry_out_pow_measur,
                                  depth_modulation=depth_modulation,
                                  ident_code=ident_code,
                                  check_antenna=check_antenna,
                                  check_ACU=check_ACU,
                                    status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper=='YEARLY':
                    check_carrier_freq = int(request.POST['check_carrier_freq'])
                    check_modulation_frq = int(request.POST['check_modulation_frq'])
                    check_monitor_alarm = int(request.POST['check_monitor_alarm'])
                    ndb_obj = NDB(check_carrier_freq=check_carrier_freq,
                                  check_modulation_frq=check_modulation_frq,
                                  check_monitor_alarm=check_monitor_alarm,
                                  status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')

            if eq_obj.equipment_name.upper() == 'DATISTERMA':
                if report_type.upper() == 'DAILY':
                    ndb_obj = Datis_Terma(status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                d_obj = Datis_Terma(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                d_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            if eq_obj.equipment_name.upper() == 'DVTR':
                if report_type.upper() == 'DAILY':
                    room_temp = int(request.POST['room_temp'])
                    AC_main_volt = int(request.POST['AC_main_volt'])
                    UPS_out_volt = int(request.POST['UPS_out_volt'])
                    cleanlines = int(request.POST['cleanlines']     )
                    status_UPS = int(request.POST['status_UPS'])
                    recording_all_channels =int( request.POST['recording_all_channels'])
                    media_staus = int(request.POST['media_staus'])
                    status_indication = int(request.POST['status_indication'])
                    status_cooling_fans = int(request.POST['status_cooling_fans'])
                    Free_space_disk = int(request.POST['Free_space_disk'])
                    ndb_obj = DVTR(room_temp=room_temp,AC_main_volt=AC_main_volt,
                          UPS_out_volt=UPS_out_volt,cleanlines=cleanlines,
                          status_UPS=status_UPS,
                          recording_all_channels=recording_all_channels,
                          media_staus=media_staus,
                          status_indication=status_indication,
                          status_cooling_fans=status_cooling_fans,
                          Free_space_disk=Free_space_disk,
                          status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                if report_type.upper() == 'MONTHLY':
                    cleaning_PC_dust = int(request.POST['cleaning_PC_dust'])
                    Check_connectors = int(request.POST['Check_connectors'])
                    check_battery_backup = int(request.POST['check_battery_backup'])
                    program_to_Check_HDD = int(request.POST['program_to_Check_HDD'])
                    Application_only_forH24 = int(request.POST['Application_only_forH24'])
                    ndb_obj = DVTR(cleaning_PC_dust=cleaning_PC_dust,
                                  Check_connectors=Check_connectors,
                                  check_battery_backup=check_battery_backup,
                                  program_to_Check_HDD=program_to_Check_HDD,
                                  Application_only_forH24=Application_only_forH24,
                                status=status, equipment_name=eq_obj.equipment_name,
                                  modal_number=eq_obj.modal_number, Make=eq_obj.company,
                                  Airport_Location=location, station_name=st_obj,
                                  created_by=user_profile,
                                  report_type=report_type.lower())
                    ndb_obj.save()
                    messages.success(request, "Saved Successfully...")
                    return redirect('/')
                ndb_obj = DVTR(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
                ndb_obj.save()
                messages.success(request, "Saved Successfully...")
                return redirect('/')
            otherEq_obj = OtherEquipmentsReport(status=status, equipment_name=eq_obj.equipment_name, modal_number=eq_obj.modal_number, Make=eq_obj.company, Airport_Location=location, station_name=st_obj, created_by=user_profile, report_type=report_type.lower())
            otherEq_obj.save()
            messages.success(request, "Saved Successfully...")
            return redirect('/')

            

def NewEntryAfterQr(request, eq_id=None, report_type=None, st_name = None):
    if request.method == 'GET':
        new_obj = Equipments.objects.filter(id=eq_id)
        eq_name = obj.equipment_name
        context = {
                 eq_name : True,
                 report_type: True,
                 'report': report_type,
                'eqobj': newobj
            }
        return render(request, 'Station&Parameter.html', context)



def Equipmentautocomplete(request):
    if 'term' in request.GET:
        qs = Equipments.objects.filter(equipment_name__icontains=request.GET.get('term'))
        equipments = list()
        for item in qs:
            equipments.append(item.equipment_name)
        # titles = [product.title for product in qs]
        return JsonResponse(equipments, safe = False)
    return render(request, "NewEntry.html")

def EquipmentSerialautocomplete(request):
    if 'term' in request.GET:
        qs = Equipments.objects.filter(serial_number__icontains=int(request.GET.get('term')))
        serials = list()
        for item in qs:
            serials.append(str(item.serial_number))
        # titles = [product.title for product in qs]
        return JsonResponse(serials, safe = False)
    return render(request, "NewEntry.html")


def EquipmentModelNumberAutocomplete(request):
    if 'term' in request.GET:
        qs = Equipments.objects.filter(modal_number__icontains=request.GET.get('term'))
        serials = list()
        for item in qs:
            serials.append(item.modal_number)
        # titles = [product.title for product in qs]
        return JsonResponse(serials, safe = False)
    return render(request, "NewEntry.html")


def EquipmentCompanyAutocomplete(request):
    if 'term' in request.GET:
        qs = Equipments.objects.filter(company__icontains=request.GET.get('term'))
        campanies = list()
        for item in qs:
            campanies.append(item.company)
        # titles = [product.title for product in qs]
        return JsonResponse(campanies, safe = False)
    return render(request, "NewEntry.html")

def StationNameAutocomplete(request):
    if 'term' in request.GET:
        qs = Stations.objects.filter(station_name__icontains=request.GET.get('term'))
        station_names = list()
        for item in qs:
            station_names.append(item.station_name)
        # titles = [product.title for product in qs]
        return JsonResponse(station_names, safe = False)
    return render(request, "NewEntry.html")