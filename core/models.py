from django.urls import reverse
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth import models as auth_models
from django.db import models as models

User = get_user_model()

REPORT_TYPE_CHOICES = [
    ('daily', 'Daily'),
    ('weekly', 'Weekly'),
    ('monthly', 'Monthly'),
    ('quarterly', 'Quaterly'),
    ('halfyearly', 'Half-Yearly'),
    ('year', 'Yearly')
]

EQUIPMENT_TYPE_CHOICES = [
    ('communication', 'Communication'),
    ('navigation', 'Navigation'),
    ('surveillance', 'Surveillance'),
]
class Airports(models.Model):

    # Fields
    Airport_Name = models.CharField(max_length=255)
    Airport_Location = models.CharField(max_length=250)
    Airport_Type = models.CharField(max_length=350)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Airport'
        verbose_name_plural = 'Airports'
        

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
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        return self.name


class Equipments(models.Model):

    # Fields
    equipment_name = models.CharField(max_length=255)
    serial_number = models.IntegerField(blank=True, null=True)
    modal_number = models.CharField(max_length=2000)
    equipment_type = models.CharField(max_length=2000, choices=EQUIPMENT_TYPE_CHOICES)
    company = models.CharField(max_length=1000)
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        verbose_name = 'Equipment'
        verbose_name_plural = 'Equipments'

    def __str__(self):
        return self.equipment_name


class Stations(models.Model):

    # Fields
    station_name = models.CharField(max_length=300)
    region = models.CharField(max_length=255)
    created_time = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    # Relationship Fields
    location = models.ForeignKey(
        Airports,
         on_delete=models.CASCADE
    )
    Number_of_equipments = models.ManyToManyField(
        Equipments, blank=True
    )

    class Meta:
        ordering = ('-created_time',)
        verbose_name = 'Station'
        verbose_name_plural = 'Stations'
        

    def __str__(self):
        return self.station_name




class Glid_Path(models.Model):
    equipment_name = models.CharField(max_length = 255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255) 
    Airport_Location = models.CharField(max_length = 255) 
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False, blank=True)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
    #Thales 
   
    
    remarks = models.CharField(max_length = 255, blank=True, null=True)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    
    '''parameter of glid path'''
    # Daily report data 
    General_cleanliness_room = models.BooleanField(blank=True, null=True)
    Status_airconditioners = models.BooleanField(blank=True, null=True)
    status_obstruction_light = models.BooleanField(blank=True, null=True)
    main_supply_volt = models.IntegerField(blank=True, null=True)
    main_supply_frequency = models.FloatField(blank=True, null=True)
    verify_equipment_on_UPS = models.BooleanField(blank=True, null=True)
    status_near_monitor = models.BooleanField(blank=True, null=True)
    status_critical_area = models.BooleanField(blank=True, null=True)
    remote_status_indication = models.BooleanField(blank=True, null=True)
    #system status indication '' normal staus = ok ''
    param = models.BooleanField(blank=True, null=True)
    Disagr = models.BooleanField(blank=True, null=True)
    batt = models.BooleanField(blank=True, null=True)
    maint = models.BooleanField(blank=True, null=True)
    standby = models.BooleanField(blank=True, null=True)
    course = models.BooleanField(blank=True, null=True)
    clearnance = models.BooleanField(blank=True, null=True)
    txtoair = models.BooleanField(blank=True, null=True)
    main = models.BooleanField(blank=True, null=True)
    smps = models.IntegerField(blank=True, null=True)
    # weekly report data 
    System_time_synch = models.CharField(max_length = 255, blank=True, null=True)
    time_of_observation_UTC = models.CharField(max_length = 255, blank=True, null=True)
    ILS_datetime_UTC = models.CharField(max_length = 255, blank=True, null=True)
    ups_out_volt = models.IntegerField(blank=True, null=True)
    ups_out_freq = models.FloatField(blank=True, null=True)
    ups_battery_volt = models.IntegerField(blank=True, null=True)
    battery_volt = models.IntegerField(blank=True, null=True)
    opearation_on_battery = models.BooleanField(blank=True, null=True)
    RMS_5volt = models.IntegerField(blank=True, null=True)
    RMS_battery = models.IntegerField(blank=True, null=True)
    PS1= models.IntegerField(blank=True, null=True)
    PS2= models.IntegerField(blank=True, null=True)
    CLR150 = models.IntegerField(blank=True, null=True)
    CLR90 = models.IntegerField(blank=True, null=True)
    COU150 = models.IntegerField(blank=True, null=True)
    COU90 = models.IntegerField(blank=True, null=True)
    #monthly data report 
    Path_augle= models.IntegerField(blank=True, null=True)
    change_in_displacement_sens = models.IntegerField(blank=True, null=True)
    clearance_signal = models.IntegerField(blank=True, null=True)
    reduciton_power = models.IntegerField(blank=True, null=True)
    total_time = models.IntegerField(blank=True, null=True)
    moitor_sys_oper = models.IntegerField(blank=True, null=True)
    all_function_remote = models.BooleanField(blank=True, null=True)
    grading_of_critical_are = models.IntegerField(blank=True, null=True)
    Envionment = models.BooleanField(blank=True, null=True)
    status_rc_lines = models.BooleanField(blank=True, null=True)

    #Quarterly data report 
    path_angle_monitor = models.BooleanField(blank=True, null=True)
    change_in_displacement = models.CharField(max_length = 255, blank=True, null=True)
    totoal_time_out_of_tolerance = models.FloatField(blank=True, null=True)
    coverage = models.FloatField(blank=True, null=True)
    carrier_modulation = models.FloatField(blank=True, null=True)


    #annual report 
    Frequency = models.FloatField(blank=True, null=True)
    unwanted_modulation = models.FloatField(blank=True, null=True)
    carrier_modulation_freq= models.FloatField(blank=True, null=True)
    carrier_modulation_homm = models.BooleanField(blank=True, null=True)
    phase_of_modulation_system = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = 'Glid Path Report'
        verbose_name_plural = 'Glid Path Reports'

    def __str__(self):
        return self.report_type

class COMSOFT(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
    Airport_Location = models.CharField(max_length = 255) 
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

    remarks = models.CharField(max_length = 255, blank=True, null=True)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
   
    
     # Daily report data 
    General_cleanliness_room = models.CharField(max_length = 255, blank=True, null=True) #satisfactory
    Status_airconditioners = models.BooleanField(blank=True, null=True) #room temp in degree cel
    status_obstruction_light = models.BooleanField(blank=True, null=True) #percent
    main_supply_volt = models.FloatField(blank=True, null=True) #volt
    main_supply_frequency = models.IntegerField(blank=True, null=True) # percentage
    verify_equipment_on_UPS = models.CharField(max_length = 255, blank=True, null=True)
    status_near_monitor = models.BooleanField(blank=True, null=True)
    status_critical_area = models.BooleanField(blank=True, null=True)
    remote_status_indication = models.BooleanField(blank=True, null=True)
    #Monthly report data 
    #Sensor configuration 
    Gps_latitude = models.FloatField(blank=True, null=True)
    GPS_longitude = models.FloatField(blank=True, null=True)
    Gps_altitude = models.FloatField(blank=True, null=True) # meter
   # power_onself test result  
    general_result = models.BooleanField(blank=True, null=True)
    GPS = models.BooleanField(blank=True, null=True)
    Temp_sensing = models.BooleanField(blank=True, null=True)
    voltage_sensing = models.BooleanField(blank=True, null=True)
    FPGA = models.BooleanField(blank=True, null=True)
    Reciever = models.BooleanField(blank=True, null=True)
    Cpu_load = models.FloatField(blank=True, null=True)
    Gps_synch = models.BooleanField(blank=True, null=True)
    #voltage & temprature 
    Intermediate_volt = models.IntegerField(blank=True, null=True)
    Gps_volt = models.IntegerField(blank=True, null=True)
    FPGA_volt = models.IntegerField(blank=True, null=True)
    DSP_Board_volt = models.IntegerField(blank=True, null=True)
    DSP_board_tmep = models.IntegerField(blank=True, null=True)
    #site monitor statics
    Signal_strength_RF_Site = models.BooleanField(blank=True, null=True)
    End_to_End_test = models.BooleanField(blank=True, null=True)
    Rx_sensitivity = models.BooleanField(blank=True, null=True)
    Test_transmission_loss = models.BooleanField(blank=True, null=True)
    Decoder_test = models.BooleanField(blank=True, null=True)
    # Device staus
    Gnd_station_staus =models.BooleanField(blank=True, null=True)
    overall_build_tst_result = models.BooleanField(blank=True, null=True)
    UTC_synchr = models.BooleanField(blank=True, null=True)
    #Quaterly maintainace 
        #preventive maintenance of ADS-B sensors
  #  ADS_B_sensor 
    Physical_check_of_Antenna =models.BooleanField(blank=True, null=True)
    Physical_check_of_GPS_Antenna =models.BooleanField(blank=True, null=True)
    Associated_cables_and_connectors = models.BooleanField(blank=True, null=True)
    Physical_ceck_pow_cable =models.BooleanField(blank=True, null=True)
        # ADS-B sensor-2
    Physical_check_Antenna = models.BooleanField(blank=True, null=True)
    Associated_cables_connectors = models.BooleanField(blank=True, null=True)
    Physical_Chk_LAN_cables = models.BooleanField(blank=True, null=True)
    Physical_chk_power_cables = models.BooleanField(blank=True, null=True)

    class Meta:
        verbose_name = 'Comsoft Report'
        verbose_name_plural = 'Comsoft reports'
    
    def __str__(self):
        return self.report_type
 

class VCS_System(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
    Airport_Location = models.CharField(max_length = 255) 
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
     #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

    remarks = models.CharField(max_length = 255, blank=True, null=True)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    
    # Daily data 
    Ac_volt_UPS1 = models.CharField(max_length = 255, blank=True, null=True)
    Condition_UPS1 = models.CharField(max_length = 255, blank=True, null=True)
    RAD1PSU= models.CharField(max_length = 255, blank=True, null=True)
    TEL1_PSU = models.CharField(max_length = 255, blank=True, null=True)
    TEL2_PSU = models.CharField(max_length = 255, blank=True, null=True)
    TEL3_PSU = models.CharField(max_length = 255,blank=True, null=True)
    TEL4_PSU = models.CharField(max_length = 255, blank=True, null=True)
    PSU_FuseLED = models.CharField(max_length = 255, blank=True, null=True)
    system_A = models.CharField(max_length = 255, blank=True, null=True)
    Overall_perform = models.CharField(max_length = 255, blank=True, null=True)
    # Weekly data 
    DMC01D5 = models.CharField(max_length = 255, blank=True, null=True)
    D5= models.CharField(max_length = 255, blank=True, null=True)
    D4= models.CharField(max_length = 255, blank=True, null=True)
    D3 = models.CharField(max_length = 255, blank=True, null=True)
    PDE_4601 = models.CharField(max_length = 255, blank=True, null=True)
    D2 = models.CharField(max_length = 255, blank=True, null=True)
    DMC02= models.CharField(max_length = 255, blank=True, null=True)
    MPC_01 = models.CharField(max_length = 255, blank=True, null=True)
    D1PDE4662= models.CharField(max_length = 255, blank=True, null=True)
   
   

    class Meta:
        verbose_name = 'Vcs System Report'
        verbose_name_plural = 'Vcs System Reports'
    
    def __str__(self):
        return self.report_type


class Localizer(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
    Airport_Location = models.CharField(max_length = 255) 
   
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)



   
    remarks = models.CharField(max_length = 255,  blank=True, null=True)
    status=  models.BooleanField( blank=True, null=True, verbose_name="Report Status")
   
    #daily field data 
    General_cleanliness_room = models.BooleanField(max_length = 255,  blank=True, null=True)
    Status_airconditioners = models.BooleanField(max_length = 255,  blank=True, null=True)
    status_obstruction_light = models.BooleanField( blank=True, null=True)
    main_supply_volt = models.IntegerField( blank=True, null=True)
    main_supply_frequency = models.FloatField( blank=True, null=True)
    # weekly field data 
    System_time_synch = models.IntegerField( blank=True, null=True)
    Time_of_observ_UTC = models.IntegerField( blank=True, null=True)
    ILS_data_UTC = models.IntegerField( blank=True, null=True)
    Time_source_synch = models.FloatField( blank=True, null=True)
            #Ups measurment 
    Ups_out_volt = models.IntegerField( blank=True, null=True)
    Ups_out_freq = models.IntegerField( blank=True, null=True)
    Ups_battery_volt = models.IntegerField( blank=True, null=True)
    Battery_volt_before_discharge = models.IntegerField( blank=True, null=True)
    operation_on_battery = models.BooleanField( blank=True, null=True)
    battery_volt = models.IntegerField( blank=True, null=True)
    Battery_terminal_cleaned = models.BooleanField( blank=True, null=True)
        #parameter to be checked at RMM
    course_LPA = models.IntegerField( blank=True, null=True)
    CSBlevel = models.IntegerField( blank=True, null=True)
    SBOlevel = models.IntegerField( blank=True, null=True)
    PH_Corr_peak_lev = models.IntegerField( blank=True, null=True)
    CLR_GPA = models.IntegerField( blank=True, null=True)
    PA27lev = models.IntegerField( blank=True, null=True)
    #weekly data filed 
        #parameter 
    course_alignment = models.CharField(max_length = 255,  blank=True, null=True)
    course_shift= models.CharField(max_length = 255,  blank=True, null=True)
    change_in_displ_sensitivity = models.CharField(max_length = 255,  blank=True, null=True)
    Reduction_pow = models.CharField(max_length = 255,  blank=True, null=True)
    Total_time_out_tolerance = models.FloatField( blank=True, null=True)
        #PhysicalInspection 
        #itemsto bechecked
    physical_inspection = models.IntegerField( blank=True, null=True)
    check_allcables_conn = models.IntegerField( blank=True, null=True)
    check_allnuts_bolt = models.IntegerField( blank=True, null=True)
    Tx_parameters_DC_pow = models.FloatField( blank=True, null=True)
        #check 
    MonitorSystemOperation = models.BooleanField( blank=True, null=True)
    All_function_remotecontrol = models.BooleanField( blank=True, null=True)
    Grading_ofcritical_area = models.IntegerField( blank=True, null=True)
    Environment_vegetaion = models.IntegerField( blank=True, null=True)
    status_RClines = models.BooleanField( blank=True, null=True)
        #Monitor integrity check 
    auto_changeover_value = models.IntegerField( blank=True, null=True)
    Auto_Shutdown = models.BooleanField( blank=True, null=True)
    PA27Level = models.IntegerField( blank=True, null=True)
    Auto_changeOver_ok = models.BooleanField( blank=True, null=True)
    Auto_shutdown_from_tx = models.IntegerField( blank=True, null=True)
            # monthly reprot data 
    ''' Earthing lighting and surge protection device (SPD)'''
    Equ_rack_earth_resis = models.IntegerField( blank=True, null=True)
    Earth_resis_antenna = models.IntegerField( blank=True, null=True)
    Earth_resis_NF_monitor_antenna = models.IntegerField( blank=True, null=True)
    Earth_resisFFM = models.IntegerField( blank=True, null=True)
    Earth_to_neutral_volt = models.IntegerField( blank=True, null=True)
        #Quaterly data report 
    Suprious_modul = models.IntegerField( blank=True, null=True)
    Coverage_dist = models.IntegerField(blank=True, null=True)
    Carrier_modulation = models.CharField(max_length = 255, blank=True, null=True)
    carrier_modul_harmonic = models.CharField(max_length = 255, blank=True, null=True)
    Carrier_module_hor_contetn = models.CharField(max_length = 255, blank=True, null=True)
    sun_modul_depths = models.IntegerField(blank=True, null=True)
    course_alignment = models.IntegerField(blank=True, null=True)
    identification = models.IntegerField(blank=True, null=True)
    identification_repetition_rate = models.IntegerField(blank=True, null=True)
        #Annual reprot data 
    Frequency = models.IntegerField(blank=True, null=True)
    carrier_modulation_freq = models.FloatField(blank=True, null=True)
    carrier_module_har_content = models.BooleanField(blank=True, null=True)
    Carrier_modulation_harm = models.IntegerField(blank=True, null=True)
    Unwanted_modulation = models.CharField(max_length = 255, blank=True, null=True)
        #Transmmitter waveform checks 
    CSB_in_watt = models.IntegerField(blank=True, null=True) #watt
    SBO = models.IntegerField(blank=True, null=True)
    phase_CORR = models.IntegerField(blank=True, null=True)
    LF_phase_check = models.BooleanField(blank=True, null=True)
    RF_phase_check = models.BooleanField(blank=True, null=True)
        #DDM/SDM checks
    DDM_check_COU = models.IntegerField(blank=True, null=True)
    SDM_check_COU = models.IntegerField(blank=True, null=True)
    Course_ident_Mod = models.BooleanField(blank=True, null=True)
        #Output power check with wattmeter
    Cou_Trans_out_pow = models.IntegerField(blank=True, null=True)
    CLR_Tranns_out_pow = models.IntegerField(blank=True, null=True)
        #Monitor delay 
    Monitor_delay = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'Localizer Report'
        verbose_name_plural = 'Localizer Reports'
    
    def __str__(self):
        return self.report_type

    


class DVOR(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255) #Thales 
    Airport_Location = models.CharField(max_length = 255) 
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
        #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

   
    remarks = models.CharField(max_length = 255, blank=True, null=True)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    
  

    # parameter to be checked in daily report 
    Equipment_shelter_cleanlines = models.BooleanField(blank=True, null=True)
    status_air_conditioners = models.BooleanField(blank=True, null=True)
    shelter_temp_in_celcius = models.FloatField(blank=True, null=True) # celcius
    UPS_input_volt_frequency = models.IntegerField(blank=True, null=True)
    PS_output_volt_frequency = models.IntegerField(blank=True, null=True)
    status_battery_operation = models.BooleanField(blank=True, null=True)
    hours_operation = models.FloatField(blank=True, null=True)
    Alarm = models.IntegerField(blank=True, null=True)

    # Weekly data 
        # Transmitter data 
    Carrier_pow = models.IntegerField(blank=True, null=True)
    AM_30hz =models.FloatField(blank=True, null=True)
    Am_1020hz =models.FloatField(blank=True, null=True)
    USB_level =models.FloatField(blank=True, null=True)
    USB_RF_Phase =models.FloatField(blank=True, null=True)
    LSB_level  = models.FloatField(blank=True, null=True)
        # Near field antenna
    Azinmuth = models.IntegerField(blank=True, null=True)
    RF_level = models.IntegerField(blank=True, null=True)
    FM_index = models.IntegerField(blank=True, null=True)
        # Internal integral 
    Carrier_frequency = models.FloatField(blank=True, null=True)
    USB_frequency  = models.FloatField(blank=True, null=True)
    LSB_frequency = models.FloatField(blank=True, null=True)
        #Alarm limit 
    Azimuth_Ul_near  = models.BooleanField(blank=True, null=True)
    Azimuth_LL_nar = models.BooleanField(blank=True, null=True)
        #battery data 
    battery_volt = models.FloatField(blank=True, null=True)
    battery_half_volt = models.FloatField(blank=True, null=True)
    battery_current = models.FloatField(blank=True, null=True)

    # Monthly data
        # status of earthing, lighting and surge protection devices
    #status of earthing system: 
    Eq_earth_rack_resistance =  models.IntegerField(blank=True, null=True)
    earth_resistance_at_antenna  = models.IntegerField(blank=True, null=True)
    earth_natural_volt = models.IntegerField(blank=True, null=True)
        #staus of lighting and surge protection 
    earth_resis_lighting = models.IntegerField(blank=True, null=True)
    status_of_lighting_protection_system = models.BooleanField(blank=True, null=True)
    status_SPD_at_eq_room  = models.BooleanField(blank=True, null=True)

    # Six mothly dvor-thales data
    # Description 
    Physical_condition_antenna = models.BooleanField(blank=True, null=True)
    ground_calibration_done_on = models.BooleanField(blank=True, null=True)
    Error_spread = models.BooleanField(blank=True, null=True)
    Verify_counter_poise = models.IntegerField(blank=True, null=True)
    Alarm_co_time = models.IntegerField(blank=True, null=True)

    # Anual  report  Dvor_Thales
    Carrier_frequency =  models.FloatField(blank=True, null=True)
    Hz_derivation = models.FloatField(blank=True, null=True)
    Hz_modulation_depth = models.FloatField(blank=True, null=True)
    Hz_modulation_frequency = models.FloatField(blank=True, null=True)
    identification_speed = models.FloatField(blank=True, null=True)
    identification_repetition = models.IntegerField(blank=True, null=True)
    identification_tone_frequency = models.FloatField(blank=True, null=True)
    Bearing_monitor = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name = 'DVOR Report'
        verbose_name_plural = 'DVOR Reports'
    
    def __str__(self):
        return self.report_type


class NDB(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255) #Thales 
    Airport_Location = models.CharField(max_length = 255) 
   
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)


  
    remarks = models.CharField(max_length = 255, blank=True, null=True)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    
    #daily data for NDB
    #general 
    room_temp = models.IntegerField(blank=True, null=True) # degree celcius 
    AC_main_volt =models.IntegerField(blank=True, null=True) # volt 
    UPS_out_volt =models.IntegerField(blank=True, null=True) # volt
    cleanlines = models.CharField(max_length = 255, blank=True, null=True) 
    # equipment checks 
    ''' same for two type of transmitter '''
    reflected_power  = models.FloatField(blank=True, null=True) # percentage  
    Forword_Power = models.FloatField(blank=True, null=True) # percentage FWD power 
    modulation = models.FloatField(blank=True, null=True) 
    PA_volt = models.IntegerField(blank=True, null=True) #volt 
    PA_current = models.IntegerField(blank=True, null=True) #volt
    # Local control panel 
    System_staus_LED   = models.BooleanField(blank=True, null=True)
    primary_tx_led = models.BooleanField(blank=True, null=True)
    tx_power_on_led = models.BooleanField(blank=True, null=True)

    # Weekly data of NDB
    main_pow_supp_terminal  = models.CharField(max_length = 255, blank=True, null=True)
    check_battery_terminal = models.BooleanField(blank=True, null=True)
    condition_of_Battery = models.BooleanField(blank=True, null=True)
    condition_of_UPS = models.BooleanField(blank=True, null=True)
    UPs_out_load = models.IntegerField(blank=True, null=True)
    condition_earthing = models.BooleanField(blank=True, null=True)
    #Monthly data 
    Carry_out_pow_measur  = models.IntegerField(blank=True, null=True)
    depth_modulation = models.IntegerField(blank=True, null=True)
    ident_code = models.IntegerField(blank=True, null=True)
    check_antenna = models.BooleanField(blank=True, null=True)
    check_ACU = models.CharField(max_length = 255, blank=True, null=True)
    #quaterly data 
    check_carrier_freq = models.FloatField(blank=True, null=True)
    check_modulation_frq = models.FloatField(blank=True, null=True)
    check_monitor_alarm = models.IntegerField(blank=True, null=True)

    class Meta:
        verbose_name = 'NDB Report'
        verbose_name_plural = 'NDB Reports'
    
    def __str__(self):
        return self.report_type



class Datis_Terma(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255) #Thales 
    Airport_Location = models.CharField(max_length = 255) 
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
        # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

    
    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    
    #daily data 
    Physical_clean =models.BooleanField(blank=True, null=True) 
    PS_A_UPS =models.CharField(max_length = 255, blank=True, null=True) 
    PS_B_UPS =models.CharField(max_length = 255, blank=True, null=True) 
    overall_A = models.CharField(max_length = 255, blank=True, null=True) 
    overall_B= models.CharField(max_length = 255, blank=True, null=True)

    class Meta:
        verbose_name = 'Datis Terma Report'
        verbose_name_plural = 'Datis Terma Reports'
    
    def __str__(self):
        return self.report_type



class DVTR(models.Model):
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
    Airport_Location = models.CharField(max_length = 255) 
   
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)

    remarks = models.CharField(max_length = 255)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    
    #daily data 
    frequency = models.CharField(max_length=8, blank=True, null=True)
    room_temp = models.IntegerField(blank=True, null=True) 
    AC_main_volt =models.IntegerField(blank=True, null=True) 
    UPS_out_volt =models.IntegerField(blank=True, null=True) 
    cleanlines = models.BooleanField(blank=True, null=True) 
     # main DVTR , attributes will also check on standby DVTR
    status_UPS = models.BooleanField(blank=True, null=True) 
    recording_all_channels = models.CharField(max_length = 255, blank=True, null=True) 
    media_staus = models.BooleanField(blank=True, null=True) 
    status_indication = models.BooleanField(blank=True, null=True) 
    status_cooling_fans = models.BooleanField(blank=True, null=True) 
    Free_space_disk = models.BooleanField(blank=True, null=True) 
    #MOnthhly data 
    cleaning_PC_dust = models.BooleanField(blank=True, null=True) 
    Check_connectors = models.BooleanField(blank=True, null=True) 
    check_battery_backup = models.BooleanField(blank=True, null=True) 
    program_to_Check_HDD = models.BooleanField(blank=True, null=True) 
    Application_only_forH24= models.IntegerField(blank=True, null=True) 

    class Meta:
        verbose_name = 'DVTR Report'
        verbose_name_plural = 'DVTR Reports'
    
    def __str__(self):
        return self.report_type


class UPS(models.Model):

    # Fields
    equipment_name = models.CharField(max_length=255)
    modal_number = models.CharField(max_length = 255)
    Make = models.CharField(max_length = 255)
    Airport_Location = models.CharField(max_length = 255) 
    
    
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    
        # Fields
    verified_by_Manager = models.BooleanField(default=False)
    # Relationship Fields
    station_name = models.ForeignKey(Stations, on_delete=models.CASCADE)
    #this is for creation Info
    created_by = models.ForeignKey(Profile, on_delete=models.CASCADE)
    
   
    remarks = models.CharField(max_length = 255,  blank=True, null=True)
    status=  models.BooleanField(blank=True, null=True, verbose_name="Report status")
    

    #Field to deteremine type of report
    report_type = models.CharField(max_length=20, choices=REPORT_TYPE_CHOICES)

    
    
    #Dail report fields
    Input_voltage = models.IntegerField(blank=True, null=True)
    Input_frequency = models.IntegerField(blank=True, null=True)
    Output_voltage = models.IntegerField(blank=True, null=True)
    output_frequency = models.IntegerField(blank=True, null=True)
    output_load = models.IntegerField(blank=True, null=True)
    Battery_bank_volt = models.IntegerField(blank=True, null=True)
    Battery_current = models.IntegerField(blank=True, null=True)
    working = models.CharField(max_length=4,  blank=True, null=True)
    
   

    # Weekly report fields
    Power_supply_terminal = models.BooleanField( blank=True, null=True)
    check_battery_terminal = models.BooleanField( blank=True, null=True)
    Battery_condition = models.BooleanField( blank=True, null=True)
    UPS_condition = models.BooleanField( blank=True, null=True)
    UPS_load_percent = models.FloatField( blank=True, null=True)
    Neutral_load = models.FloatField( blank=True, null=True)
    Earthing_codition = models.BooleanField( blank=True, null=True)

    #monthly report fields
    Physicaly_clean_check =models.BooleanField( blank=True, null=True)
    Rx_module_status = models.BooleanField( blank=True, null=True)
    Control_Panel_setup  = models.BooleanField( blank=True, null=True)
    Physica_check_antenna_cables = models.BooleanField( blank=True, null=True)
    DAT_drive_cleaning = models.BooleanField(blank=True, null=True)
    Netuno_Server_restart = models.BooleanField(blank=True, null=True)
    
    # Relationship Field   

    class Meta:
        verbose_name = 'Ups Report'
        verbose_name_plural = 'Ups Reports'
    
    def __str__(self):
        return self.report_type






