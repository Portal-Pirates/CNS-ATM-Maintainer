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
    list_display = ['equipment_name', 'modal_number','station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name__station_name', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

    #Sections in forms

    fieldsets = [
        # BAsic details
        ("Basic Details", {'fields': [
         "equipment_name", "modal_number", "Make", "Airport_Location", "verified_by_Manager", "station_name", "created_by", "report_type"]}),
       
       #Kuch iss type se daily weekly etc parameters tuples
        ("Daily Parameters", {"fields": ["Nominal_value_ohm", 'measured_value_ohm', 'status','remarks']}),
      
    ]


@admin.register(COMSOFT)

class COMSOFTAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40


@admin.register(VCS_System)
class VCS_SystemAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40


@admin.register(Localizer)

class LocalizerAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'station_name','Airport_Location','verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

@admin.register(DVOR)

class DVORAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'station_name','Airport_Location','verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40


@admin.register(NDB)

class NDBAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number','station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40


@admin.register(Datis_Terma)

class Datis_TermaAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number','station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40

@admin.register(DVTR)

class DVTRAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40




@admin.register(UPS)
class UPSAdmin(admin.ModelAdmin):
    list_display = ['equipment_name', 'modal_number', 'station_name','Airport_Location', 'verified_by_Manager', 'created_by', 'report_type', 'Make']
    list_filter = ['report_type', 'station_name', 'Airport_Location', 'created_by', 'Make']
    search_fields = ['modal_number', 'station_name', 'report_type']
    list_per_page = 40


