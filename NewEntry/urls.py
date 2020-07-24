from django.conf.urls import url
from django.urls import path
from .views import EquipmentNewEntry, select_type, Equipmentautocomplete, Equipmentdetail


urlpatterns = [
    path('select_type', select_type, name='select_type' ),
    path('<str:report_type>', EquipmentNewEntry, name="EquipmentNewEntry"),
    path('Equipmentdetail/<str:report_type>', Equipmentdetail, name="Equipmentdetail"),
    path('ajax/equipments', Equipmentautocomplete, name='Equipmentautocomplete'),

]
