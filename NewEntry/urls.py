from django.conf.urls import url
from django.urls import path
from .views import NewEntry, StationNameAutocomplete, EquipmentCompanyAutocomplete, EquipmentModelNumberAutocomplete,EquipmentSerialautocomplete, EquipmentNewEntry, select_type, Equipmentautocomplete, Equipmentdetail


urlpatterns = [
    path('select_type', select_type, name='select_type' ),
    path('<str:report_type>', EquipmentNewEntry, name="EquipmentNewEntry"),
    path('Equipmentdetail/<str:report_type>', Equipmentdetail, name="Equipmentdetail"),
    path('add/<int:id>/<str:report_type>', NewEntry, name="NewEntry"),
    path('ajax/equipments', Equipmentautocomplete, name='Equipmentautocomplete'),
    path('ajax/EquipmentSerialautocomplete', EquipmentSerialautocomplete, name='EquipmentSerialautocomplete'),
    path('ajax/EquipmentModelNumberAutocomplete', EquipmentModelNumberAutocomplete, name='EquipmentModelNumberAutocomplete'),
    path('ajax/EquipmentCompanyAutocomplete', EquipmentCompanyAutocomplete, name='EquipmentCompanyAutocomplete'),
    path('ajax/StationNameAutocomplete', StationNameAutocomplete, name='StationNameAutocomplete'),
]