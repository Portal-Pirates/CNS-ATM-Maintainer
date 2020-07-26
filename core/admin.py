from django.contrib import admin
from .models import *


admin.site.site_header = "Admin View of AAI Maintaince"
admin.site.site_title = "Admin View of AAI Maintaince" 
admin.site.index_title =  "My Admin"

#Custumizations on Admin View

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'working_location', 'is_manager', 'created']
    list_filter = ['working_location', 'is_manager']
    search_fields = ['name']
    list_per_page = 40


@admin.register(Airports)
class AirportsAdmin(admin.ModelAdmin):
    list_display = ['Airport_Name', 'Airport_Location', 'Airport_Type']
    list_filter = ['Airport_Name', 'Airport_Location', 'Airport_Type']
    search_fields = ['Airport_Name', 'Airport_Location']
    list_per_page = 40



@admin.register(Stations)

class StationsAdmin(admin.ModelAdmin):
    list_display = ['station_name', 'region', 'location']
    list_filter = ['location', 'region']
    search_fields = ['station_name', 'region']
    list_per_page = 40



@admin.register(Equipments)

class EquipmentsAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'serial_number', 'modal_number', 'equipment_type', 'company']
    list_filter = ['equipment_type', 'company', 'equipment_name']
    search_fields = ['serial_number', 'modal_number', 'equipment_name']
    list_per_page = 40


# Now all Equipments below
@admin.register(Glid_Path)

class Glid_PathAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40
    # section
    fieldsets = [
        ("Basic-Details",{'fields':["equipment_name","modal_number","Make","Airport_Location","verified_by_Manager","station_name","created_by","report_type"]}),
        ("Daily-Parameters",{"fields":["General_cleanliness_room","Status_airconditioners","status_obstruction_light",
                                        "main_supply_volt","main_supply_frequency","verify_equipment_on_UPS","status_near_monitor",
                                        "status_critical_area","remote_status_indication","param","Disagr",
                                        "batt","maint","standby","course","clearnance","txtoair","main","smps"]}),
        ("Weekly-Parameters",{"fields":["System_time_synch","time_of_observation_UTC","ILS_datetime_UTC","ups_out_volt",
                                        "ups_out_freq","ups_battery_volt","battery_volt","opearation_on_battery","RMS_5volt","RMS_battery",
                                        "PS1","PS2","CLR90","COU150","COU90"]}),
        ("Monthy-Parameters",{"fields":["Path_augle","change_in_displacement_sens","clearance_signal","reduciton_power","total_time","moitor_sys_oper",
                                        "all_function_remote","grading_of_critical_are","Envionment","status_rc_lines"]}),
        ("Quaterly-Parameters",{"fields":["path_angle_monitor","change_in_displacement","totoal_time_out_of_tolerance","coverage","carrier_modulation"]}),
        ("Annual-Parameters",{"fields":["Frequency","unwanted_modulation","carrier_modulation_freq","carrier_modulation_homm","phase_of_modulation_system"]})

    ]


@admin.register(COMSOFT)

class COMSOFTAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",{'fields':["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                                   "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter",{'fields':['General_cleanliness_room','Status_airconditioners','status_obstruction_light','main_supply_volt','main_supply_frequency','verify_equipment_on_UPS','status_near_monitor','status_critical_area','remote_status_indication']}),
                 ("Monthly-Parameter",{'fields':['Gps_latitude','GPS_longitude','Gps_altitude','general_result','GPS','voltage_sensing','FPGA','Reciever','Cpu_load','Gps_synch','Intermediate_volt',
                                                'Gps_volt','FPGA_volt','DSP_Board_volt','DSP_board_tmep','Signal_strength_RF_Site','End_to_End_test',
    'Rx_sensitivity',
    'Test_transmission_loss',
    'Decoder_test',
    'Gnd_station_staus',
    'overall_build_tst_result',
    'UTC_synchr']}),
                 ("Quraterly-Parameter",{'fields':['Physical_check_of_Antenna','Physical_check_of_GPS_Antenna','Associated_cables_and_connectors','Physical_ceck_pow_cable','Physical_check_Antenna',
                                                    'Associated_cables_connectors','Physical_Chk_LAN_cables','Physical_chk_power_cables']})
                 ]


@admin.register(VCS_System)

class VCS_SystemAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",
                  {'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter", {'fields':['Ac_volt_UPS1','Condition_UPS1','RAD1PSU','TEL1_PSU','TEL2_PSU','TEL3_PSU','TEL4_PSU',
                                                'PSU_FuseLED','system_A','Overall_perform']}),
                 ("Weekly-Parameter",{'fields':['DMC01D5','D5','D4','D3','PDE_4601','D2',
                                                'DMC02','PDE4601','MPC_01','D1PDE4662',
                                                ]})
                 ]


@admin.register(Localizer)

class LocalizerAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40
    
    fieldsets = [("Basic-Details",{'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter", {'fields': ['General_cleanliness_room',
                                                 'Status_airconditioners',
                                                 'status_obstruction_light',
                                                 'main_supply_volt',
                                                 'main_supply_frequency']}),
                 ("Weekly-Parameter",{'fields':['System_time_synch','Time_of_observ_UTC',
                                                'ILS_data_UTC','Time_source_synch',
                                                'Ups_out_volt','Ups_out_freq',
                                                'Ups_battery_volt','Battery_volt_before_discharge',
                                                'operation_on_battery','Battery_terminal_cleaned',
                                                'course_LPA','CSBlevel','SBOlevel',
                                                'PH_Corr_peak_lev','CLR_GPA',
                                                'course_shift',
                                                'change_in_displ_sensitivity','Reduction_pow',
                                                'Total_time_out_tolerance','physical_inspection',
                                                'check_allcables_conn','check_allnuts_bolt',
                                                'Tx_parameters_DC_pow','MonitorSystemOperation',
                                                'All_function_remotecontrol','Grading_ofcritical_area',
                                                'Environment_vegetaion','status_RClines','auto_changeover_value','PA27Leval',
                                                'PA27Level','Auto_changeOver_ok','Auto_shutdown_from_tx']}),
                 ("Monthly-Parameter",{'fields':['Equ_rack_earth_resis','Earth_resis_antenna','Earth_resis_NF_monitor_antenna',
                                                 'Earth_resisFFM','Earth_to_neutral_volt']}),
                 ("Quaterly-Parameter",{'fields':['Suprious_modul','Coverage_dist','Carrier_modulation','carrier_modul_harmonic',
                                                  'Carrier_module_hor_contetn','sun_modul_depths','course_alignment','identification',
                                                  'identification_repetition_rate']}),
                 ("Annual-Parameter",{'fields':['Frequency','carrier_modulation_freq','carrier_module_har_content',
                                                'Carrier_modulation_harm','Unwanted_modulation','CSB_in_watt',
                                                'SBO','phase_CORR','LF_phase_check','RF_phase_check',
                                                'DDM_check_COU','SDM_check_COU','Course_ident_Mod','Cou_Trans_out_pow',
                                                'CLR_Tranns_out_pow','Monitor_delay']})


                 ]

@admin.register(DVOR)

class DVORAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",
                  {'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter",{'fields': ['Equipment_shelter_cleanlines','status_air_conditioners','shelter_temp_in_celcius','UPS_input_volt_frequency','PS_output_volt_frequency','status_battery_operation',
                                                 'hours_operation','Alarm','remarks']}),
                 ("Weekly-Parameter",{'fields':['Carrier_pow','AM_30hz','Am_1020hz',
                                                'USB_level','USB_RF_Phase','LSB_level','Azinmuth','RF_level','FM_index','Carrier_frequency',
                                                'USB_frequency','LSB_frequency','Azimuth_Ul_near','Azimuth_LL_nar','battery_volt',
                                                'battery_half_volt','battery_current']}),
                 ("Monthly-Parameter",{'fields':['Eq_earth_rack_resistance','earth_resistance_at_antenna','earth_natural_volt','earth_resis_lighting',
                                                 'status_of_lighting_protection_system','status_SPD_at_eq_room']}),
                 ("Six-Monthly Parameter",{'fields':['Physical_condition_antenna','ground_calibration_done_on','Error_spread','Verify_counter_poise',
                                                     'Alarm_co_time']}),
                 ("Annual-Parameter",{'fields':['Hz_derivation','Hz_modulation_depth','Hz_modulation_frequency','identification_speed','identification_repetition','identification_tone_frequency',
                                                'Bearing_monitor']})
                 ]




@admin.register(NDB)

class NDBAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",
                  {'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter", {'fields': ['room_temp','AC_main_volt','UPS_out_volt','cleanlines',
                                                 'reflected_power','Forword_Power','modulation','PA_volt',
                                                 'PA_current','System_staus_LED','primary_tx_led','tx_power_on_led']}),
                 ("Weekly-Parameter",{'fields':['main_pow_supp_terminal','check_battery_terminal','condition_of_Battery','condition_of_UPS','UPs_out_load',
                                                'condition_earthing']}),
                 ("Monthly-Parameter",{'fields':['Carry_out_pow_measur','depth_modulation','ident_code','check_antenna','check_ACU']}),
                 ("Quaterly-Parameter",{'fields':[ 'check_carrier_freq','check_modulation_frq','check_monitor_alarm']})
                 ]


@admin.register(Datis_Terma)

class Datis_TermaAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",
                  {'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter", {'fields': ['Physical_clean','PS_A_UPS','PS_B_UPS','overall_A','overall_B']})
                    ]

@admin.register(DVTR)

class DVTRAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",
                  {'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter", {'fields': ['frequency','room_temp','AC_main_volt','UPS_out_volt',
    'cleanlines',
    'status_UPS',
    'recording_all_channels',
    'media_staus',
    'status_indication',
    'status_cooling_fans',
    'Free_space_disk']}),
                 ("Monthly-Parameter",{'fields':['cleaning_PC_dust',
    'Check_connectors',
    'check_battery_backup',
    'program_to_Check_HDD',
    'Application_only_forH24']})
   ]

@admin.register(UPS)
class UPSAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    fieldsets = [("Basic-Details",
                  {'fields': ["equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager",
                              "station_name", "created_by", "report_type"]}),
                 ("Daily-Parameter", {'fields': ['Input_voltage','Input_frequency','Output_voltage',
                                                 'output_frequency','output_load','Battery_bank_volt','Battery_current',
                                                'working']}),
                 ("Weekly-Parameter",{'fields':['Power_supply_terminal','check_battery_terminal','Battery_condition',
                                      'UPS_condition','UPS_load_percent','Neutral_load','Earthing_codition']}),
                 ("Monthly-Parameter",{'fields':['Physicaly_clean_check','Rx_module_status','Control_Panel_setup','Physica_check_antenna_cables','remarks',
                                                 'DAT_drive_cleaning','Netuno_Server_restart']})
                ]
