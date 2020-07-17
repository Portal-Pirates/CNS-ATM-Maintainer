from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models

User = get_user_model()

REPORT_TYPE_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('mothly', 'Monthly'),
    ('quarterly', 'Quaterly'),
    ('halfyearly', 'Half-Yearly'),
    ('year', 'Yearly')
]
class Airports(models.Model):

    # Fields
    Airport_Name = models.CharField(max_length=255)
    Airport_Location = models.CharField(max_length=250)
    Airport_Type = models.CharField(max_length=350)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        ordering = ('-pk',)
        

    def __str__(self):
        return self.Airport_Location


class Profile(models.Model):

    # Fields
    name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to="images")
    is_manager = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    user = models.OneToOneField(
        User,on_delete=models.CASCADE
    )
    working_location = models.ForeignKey(
        Airports,on_delete=models.CASCADE
    )

    class Meta:
        pass

    def __str__(self):
        return self.name


class Equipments(models.Model):

    # Fields
    equipment_name = models.CharField(max_length=255)
    serial_number = models.IntegerField()
    modal_number = models.CharField(max_length=2000)
    equipment_type = models.CharField(max_length=2000)
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return self.slug


class Stations(models.Model):

    # Fields
    station_name = models.CharField(max_length=300)
    station_location = models.CharField(max_length=300)
    slug = models.SlugField(blank=True)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    location = models.ForeignKey(
        Airports,
         on_delete=models.CASCADE
    )
    Number_of_equipments = models.ManyToManyField(
        Equipments
    )

    class Meta:
        ordering = ('-created_time',)

    def __str__(self):
        return self.slug




class Glid_Path(models.Model):
    equipment_name = models.CharField(max_length = 255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255) 
    slug = models.SlugField(blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    #Thales 
   
    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
    '''parameter of glid path'''
    # Daily report data 
    General_cleanliness_room = models.BooleanField()
    Status_airconditioners = models.IntegerField()
    status_obstruction_light = models.IntegerField()
    main_supply_volt = models.IntegerField()
    main_supply_frequency = models.FloatField()
    verify_equipment_on_UPS = models.BooleanField()
    status_near_monitor = models.BooleanField()
    status_critical_area = models.BooleanField()
    remote_status_indication = models.BooleanField()
    #system status indication '' normal staus = ok ''
    param = models.BooleanField()
    Disagr = models.BooleanField()
    batt = models.BooleanField()
    maint = models.BooleanField()
    standby = models.BooleanField()
    course = models.BooleanField()
    clearnance = models.BooleanField()
    txtoair = models.BooleanField()
    main = models.BooleanField()
    smps = models.IntegerField()
    # weekly report data 
    System_time_synch = models.CharField(max_length = 255)
    time_of_observation_UTC = models.CharField(max_length = 255)
    ILS_datetime_UTC = models.CharField(max_length = 255)
    ups_out_volt = models.IntegerField()
    ups_out_freq = models.FloatField()
    ups_battery_volt = models.IntegerField()
    battery_volt = models.IntegerField()
    opearation_on_battery = models.BooleanField()
    RMS_5volt = models.IntegerField()
    RMS_battery = models.IntegerField()
    PS1= models.IntegerField()
    PS2= models.IntegerField()
    CLR150 = models.IntegerField()
    CLR90 = models.IntegerField()
    COU150 = models.IntegerField()
    COU90 = models.IntegerField()
    #monthly data report 
    Path_augle= models.IntegerField()
    change_in_displacement_sens = models.IntegerField()
    clearance_signal = models.IntegerField()
    reduciton_power = models.IntegerField()
    total_time = models.IntegerField()
    moitor_sys_oper = models.IntegerField()
    all_function_remote = models.BooleanField()
    grading_of_critical_are = models.IntegerField()
    Envionment = models.BooleanField()
    status_rc_lines = models.BooleanField()

    #Quarterly data report 
    path_angle_monitor = models.BooleanField()
    change_in_displacement = models.CharField(max_length = 255)
    totoal_time_out_of_tolerance = models.FloatField()
    coverage = models.FloatField()
    carrier_modulation = models.FloatField()


    #annual report 
    Frequency = models.FloatField()
    unwanted_modulation = models.FloatField()
    carrier_modulation_freq= models.FloatField()
    carrier_modulation_homm = models.BooleanField()
    phase_of_modulation_system = models.BooleanField()


class COMSOFT(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField(blank=True)
    frequency = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
    # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)


    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
    
     # Daily report data 
    General_cleanliness_room = models.CharField(max_length = 255) #satisfactory
    Status_airconditioners = models.IntegerField() #room temp in degree cel
    status_obstruction_light = models.IntegerField() #percent
    main_supply_volt = models.FloatField() #volt
    main_supply_frequency = models.IntegerField() # percentage
    verify_equipment_on_UPS = models.CharField(max_length = 255)
    status_near_monitor = models.BooleanField()
    status_critical_area = models.BooleanField()
    remote_status_indication = models.BooleanField()
    #Monthly report data 
    #Sensor configuration 
    Gps_latitude = models.FloatField()
    GPS_longitude = models.FloatField()
    Gps_altitude = models.FloatField() # meter
   # power_onself test result  
    general_result = models.BooleanField()
    GPS = models.BooleanField()
    Temp_sensing = models.BooleanField()
    voltage_sensing = models.BooleanField()
    FPGA = models.BooleanField()
    Reciever = models.BooleanField()
    Cpu_load = models.FloatField()
    GPS_status = models.BooleanField()
    Gps_synch = models.BooleanField()
    #voltage & temprature 
    Intermediate_volt = models.IntegerField()
    Gps_volt = models.IntegerField()
    FPGA_volt = models.IntegerField()
    DSP_Board_volt = models.IntegerField()
    DSP_board_tmep = models.IntegerField()
    #site monitor statics
    Signal_strength_RF_Site = models.BooleanField()
    End_to_End_test = models.BooleanField()
    Rx_sensitivity = models.BooleanField()
    Test_transmission_loss = models.BooleanField()
    Decoder_test = models.BooleanField()
    # Device staus
    Gnd_station_staus =models.BooleanField()
    overall_build_tst_result = models.BooleanField()
    UTC_synchr = models.BooleanField()
    #Quaterly maintainace 
        #preventive maintenance of ADS-B sensors
  #  ADS_B_sensor 
    Physical_check_of_Antenna =models.BooleanField()
    Physical_check_of_GPS_Antenna =models.BooleanField()
    Associated_cables_and_connectors = models.BooleanField()
    Physical_ceck_pow_cable =models.BooleanField()
        # ADS-B sensor-2
    Physical_check_Antenna = models.BooleanField()
    Associated_cables_connectors = models.BooleanField()
    Physical_Chk_LAN_cables = models.BooleanField()
    Physical_chk_power_cables = models.BooleanField()
 

class VCS_System(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    frequency = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
     #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)


    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
    # Daily data 
    Ac_volt_UPS1 = models.CharField(max_length = 255)
    Condition_UPS1 = models.CharField(max_length = 255)
    RAD1PSU= models.CharField(max_length = 255)
    TEL1_PSU = models.CharField(max_length = 255)
    TEL2_PSU = models.CharField(max_length = 255)
    TEL3_PSU = models.CharField(max_length = 255)
    TEL4_PSU = models.CharField(max_length = 255)
    PSU_FuseLED = models.CharField(max_length = 255)
    system_A = models.CharField(max_length = 255)
    Overall_perform = models.CharField(max_length = 255)
    # Weekly data 
    DMC01D5 = models.CharField(max_length = 255)
    D5= models.CharField(max_length = 255)
    D4= models.CharField(max_length = 255)
    D3 = models.CharField(max_length = 255)
    PDE_4601 = models.CharField(max_length = 255)
    D2 = models.CharField(max_length = 255)
    DMC02= models.CharField(max_length = 255)
    D5 = models.CharField(max_length = 255)
    D4 = models.CharField(max_length = 255)
    D3 = models.CharField(max_length = 255)
    PDE4601= models.CharField(max_length = 255)
    D2 = models.CharField(max_length = 255)
    MPC_01 = models.CharField(max_length = 255)
    D1PDE4662= models.CharField(max_length = 255)
    D2 = models.CharField(max_length = 255)
    D4 = models.CharField(max_length = 255)


class Localizer(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)



    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
    #daily field data 
    General_cleanliness_room = models.CharField(max_length = 255)
    Status_airconditioners = models.CharField(max_length = 255)
    status_obstruction_light = models.BooleanField()
    main_supply_volt = models.IntegerField()
    main_supply_frequency = models.FloatField()
    # weekly field data 
    System_time_synch = models.IntegerField()
    Time_of_observ_UTC = models.IntegerField()
    ILS_data_UTC = models.IntegerField()
    Time_source_synch = models.FloatField()
            #Ups measurment 
    Ups_out_volt = models.IntegerField()
    Ups_out_freq = models.IntegerField()
    Ups_battery_volt = models.IntegerField()
    Battery_volt_before_discharge = models.IntegerField()
    operation_on_battery = models.BooleanField()
    battery_volt = models.IntegerField()
    Battery_terminal_cleaned = models.BooleanField()
        #parameter to be checked at RMM
    course_LPA = models.IntegerField()
    CSBlevel = models.IntegerField()
    SBOlevel = models.IntegerField()
    PH_Corr_peak_lev = models.IntegerField()
    CLR_GPA = models.IntegerField()
    PA27lev = models.IntegerField()
    CSBlevel= models.IntegerField()
    #weekly data filed 
        #parameter 
    course_alignment = models.CharField(max_length = 255)
    course_shift= models.CharField(max_length = 255)
    change_in_displ_sensitivity = models.CharField(max_length = 255)
    Reduction_pow = models.CharField(max_length = 255)
    Total_time_out_tolerance = models.FloatField()
        #PhysicalInspection 
        #itemsto bechecked
    physical_inspection = models.IntegerField()
    check_allcables_conn = models.IntegerField()
    check_allnuts_bolt = models.IntegerField()
    Tx_parameters_DC_pow = models.FloatField()
        #check 
    MonitorSystemOperation = models.BooleanField()
    All_function_remotecontrol = models.BooleanField()
    Grading_ofcritical_area = models.IntegerField()
    Environment_vegetaion = models.IntegerField()
    status_RClines = models.BooleanField()
        #Monitor integrity check 
    auto_changeover_value = models.IntegerField()
    PA27Leval= models.IntegerField()
    Auto_Shutdown = models.BooleanField()
    PA27Level = models.IntegerField()
    Auto_changeOver_ok = models.BooleanField()
    Auto_shutdown_from_tx = models.IntegerField()
            # monthly reprot data 
    ''' Earthing lighting and surge protection device (SPD)'''
    Equ_rack_earth_resis = models.IntegerField()
    Earth_resis_antenna = models.IntegerField()
    Earth_resis_NF_monitor_antenna = models.IntegerField()
    Earth_resisFFM = models.IntegerField()
    Earth_to_neutral_volt = models.IntegerField()
        #Quaterly data report 
    Suprious_modul = models.IntegerField()
    Coverage_dist = models.IntegerField()
    Carrier_modulation = models.CharField(max_length = 255)
    carrier_modul_harmonic = models.CharField(max_length = 255)
    Carrier_module_hor_contetn = models.CharField(max_length = 255)
    sun_modul_depths = models.IntegerField()
    course_alignment = models.IntegerField()
    identification = models.IntegerField()
    identification_repetition_rate = models.IntegerField()
        #Annual reprot data 
    Frequency = models.IntegerField()
    carrier_modulation_freq = models.FloatField()
    carrier_module_har_content = models.BooleanField()
    Carrier_modulation_harm = models.IntegerField()
    Unwanted_modulation = models.CharField(max_length = 255)
        #Transmmitter waveform checks 
    CSB_in_watt = models.IntegerField() #watt
    SBO = models.IntegerField()
    phase_CORR = models.IntegerField()
    LF_phase_check = models.BooleanField()
    LF_phase_check = models.BooleanField()
    RF_phase_check = models.BooleanField()
        #DDM/SDM checks
    DDM_check_COU = models.IntegerField()
    SDM_check_COU = models.IntegerField()
    Course_ident_Mod = models.BooleanField()
        #Output power check with wattmeter
    Cou_Trans_out_pow = models.IntegerField()
    CLR_Tranns_out_pow = models.IntegerField()
        #Monitor delay 
    Monitor_delay = models.IntegerField()


class DVOR(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    frequency = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255) #Thales 
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
  

    # parameter to be checked in daily report 
    Equipment_shelter_cleanlines = models.BooleanField()
    status_air_conditioners = models.BooleanField()
    shelter_temp_in_celcius = models.FloatField() # celcius
    UPS_input_volt_frequency = models.IntegerField()
    PS_output_volt_frequency = models.IntegerField()
    status_battery_operation = models.BooleanField()
    hours_operation = models.FloatField()
    Alarm = models.IntegerField()
    remark = models.CharField(max_length = 255)

    # Weekly data 
        # Transmitter data 
    Carrier_pow = models.IntegerField()
    AM_30hz =models.FloatField()
    Am_1020hz =models.FloatField()
    USB_level =models.FloatField()
    USB_RF_Phase =models.FloatField()
    LSB_level  = models.FloatField()
        # Near field antenna
    Azinmuth = models.IntegerField()
    RF_level = models.IntegerField()
    FM_index = models.IntegerField()
        # Internal integral 
    Carrier_frequency = models.FloatField()
    USB_frequency  = models.FloatField()
    LSB_frequency = models.FloatField()
        #Alarm limit 
    Azimuth_Ul_near  = models.BooleanField()
    Azimuth_LL_nar = models.BooleanField()
        #battery data 
    battery_volt = models.FloatField()
    battery_half_volt = models.FloatField()
    battery_current = models.FloatField()

    # Monthly data
        # status of earthing, lighting and surge protection devices
    #status of earthing system: 
    Eq_earth_rack_resistance =  models.IntegerField()
    earth_resistance_at_antenna  = models.IntegerField()
    earth_natural_volt = models.IntegerField()
        #staus of lighting and surge protection 
    earth_resis_lighting = models.IntegerField()
    status_of_lighting_protection_system = models.BooleanField()
    status_SPD_at_eq_room  = models.BooleanField()

    # Six mothly dvor-thales data
    # Description 
    Physical_condition_antenna = models.BooleanField(max_length = 5)
    ground_calibration_done_on = models.BooleanField(max_length = 5)
    Error_spread = models.BooleanField(max_length = 5)
    Verify_counter_poise = models.IntegerField()
    Alarm_co_time = models.IntegerField()

    # Anual  report  Dvor_Thales
    Carrier_frequency =  models.FloatField(max_length = 5)
    Hz_derivation = models.FloatField(max_length = 5)
    Hz_modulation_depth = models.FloatField(max_length = 5)
    Hz_modulation_frequency = models.FloatField(max_length = 5)
    identification_speed = models.FloatField(max_length = 5)
    identification_repetition = models.IntegerField()
    identification_tone_frequency = models.FloatField(max_length = 5)
    Bearing_monitor = models.FloatField(max_length = 5)


class NDB(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    frequency = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Region = models.CharField(max_length = 255) 
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)


    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
    #daily data for NDB
    #general 
    room_temp = models.IntegerField() # degree celcius 
    AC_main_volt =models.IntegerField() # volt 
    UPS_out_volt =models.IntegerField() # volt
    cleanlines = models.CharField(max_length = 255) 
    # equipment checks 
    ''' same for two type of transmitter '''
    reflected_power  = models.FloatField() # percentage  
    Forword_Power = models.FloatField() # percentage FWD power 
    modulation = models.FloatField() 
    PA_volt = models.IntegerField() #volt 
    PA_current = models.IntegerField() #volt
    # Local control panel 
    System_staus_LED   = models.BooleanField()
    primary_tx_led = models.BooleanField()
    tx_power_on_led = models.BooleanField()

    # Weekly data of NDB
    main_pow_supp_terminal  = models.CharField(max_length = 255)
    check_battery_terminal = models.BooleanField()
    condition_of_Battery = models.BooleanField()
    condition_of_UPS = models.BooleanField()
    UPs_out_load = models.IntegerField()
    condition_earthing = models.BooleanField()
    #Monthly data 
    Carry_out_pow_measur  = models.IntegerField()
    depth_modulation = models.IntegerField()
    ident_code = models.IntegerField()
    check_antenna = models.BooleanField()
    check_ACU = models.CharField(max_length = 255)
    #quaterly data 
    check_carrier_freq = models.FloatField()
    check_modulation_frq = models.FloatField()
    check_monitor_alarm = models.IntegerField()


class Datis_Terma(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    frequency = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Region = models.CharField(max_length = 255) 
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)


    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()
    #daily data 
    Physical_clean =models.BooleanField() 
    PS_A_UPS =models.CharField(max_length = 255) 
    PS_B_UPS =models.CharField(max_length = 255) 
    overall_A = models.CharField(max_length = 255) 
    overall_B= models.CharField(max_length = 255)


class DVTR(models.Model):
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    frequency = models.CharField(max_length=8)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    Region = models.CharField(max_length = 255)

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)


    #daily data 
    room_temp = models.IntegerField() 
    AC_main_volt =models.IntegerField() 
    UPS_out_volt =models.IntegerField() 
    cleanlines = models.BooleanField() 
     # main DVTR , attributes will also check on standby DVTR
    status_UPS = models.BooleanField() 
    recording_all_channels = models.CharField(max_length = 255) 
    media_staus = models.BooleanField() 
    status_indication = models.BooleanField() 
    status_cooling_fans = models.BooleanField() 
    Free_space_disk = models.BooleanField() 
    #MOnthhly data 
    cleaning_PC_dust = models.BooleanField() 
    Check_connectors = models.BooleanField() 
    check_battery_backup = models.BooleanField() 
    program_to_Check_HDD = models.BooleanField() 
    Application_only_forH24= models.IntegerField() 


class UPS(models.Model):

    # Fields
    eq_name = models.CharField(max_length=255)
    station = models.CharField(max_length = 10)
    slug = models.SlugField( blank=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    modal_number = models.CharField(max_length = 255)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False, editable=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    Nominal_value_ohm = models.IntegerField()
    measured_value_ohm = models.IntegerField()
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField()
    value = models.IntegerField()
    observation = models.IntegerField()
    measured_data = models.IntegerField()

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

    
    
    #Dail report fields
    Input_voltage = models.IntegerField()
    Input_frequency = models.IntegerField()
    Output_voltage = models.IntegerField()
    output_frequency = models.IntegerField()
    output_load = models.IntegerField()
    Battery_bank_volt = models.IntegerField()
    Battery_current = models.IntegerField()
    working = models.CharField(max_length=4)
    slug = models.SlugField(blank=True)
   

    # Weekly report fields
    Power_supply_terminal = models.BooleanField(max_length=4)
    check_battery_terminal = models.BooleanField(max_length=4)
    Battery_condition = models.BooleanField(max_length=4)
    UPS_condition = models.BooleanField(max_length=4)
    UPS_load_percent = models.FloatField(max_length=5)
    Neutral_load = models.FloatField(max_length=4)
    Earthing_codition = models.BooleanField(max_length=5)

    #monthly report fields
    Physicaly_clean_check =models.BooleanField(max_length=5)
    Rx_module_status = models.BooleanField(max_length=5)
    Control_Panel_setup  = models.BooleanField(max_length=5)
    Physica_check_antenna_cables = models.BooleanField(max_length=5)
    remarks = models.CharField(max_length=225)
    DAT_drive_cleaning = models.BooleanField(max_length=5)
    Netuno_Server_restart = models.BooleanField(max_length=5)
    

   



    # Relationship Field   

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return self.slug







