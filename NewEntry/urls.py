from django.conf.urls import url
from django.urls import path
from .views import *


urlpatterns = [
    path('select_type', select_type, name='select_type' ),
    path('select_type/<int:eq_id>/<str:report_type>/<str:st_name>', chooseReportAfterQr, name='chooseReportAfterQr' ),
    path('<str:report_type>', EquipmentNewEntry, name="EquipmentNewEntry"),
    path('Equipmentdetail/<str:report_type>', Equipmentdetail, name="Equipmentdetail"),
    path('add/<int:id>/<str:report_type>', NewEntry, name="NewEntry"),
    path('add/<int:eq_id>/<str:report_type>/<str:st_name>', NewEntryAfterQr, name="NewEntryAfterQr"),
    path('ajax/equipments', Equipmentautocomplete, name='Equipmentautocomplete'),
    path('ajax/EquipmentSerialautocomplete', EquipmentSerialautocomplete, name='EquipmentSerialautocomplete'),
    path('ajax/EquipmentModelNumberAutocomplete', EquipmentModelNumberAutocomplete, name='EquipmentModelNumberAutocomplete'),
    path('ajax/EquipmentCompanyAutocomplete', EquipmentCompanyAutocomplete, name='EquipmentCompanyAutocomplete'),
    path('ajax/StationNameAutocomplete', StationNameAutocomplete, name='StationNameAutocomplete'),
    path('predictdata/datatata', predictdata, name="predictdata")
]