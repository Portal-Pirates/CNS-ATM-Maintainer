from django import forms


class SearchForm(forms.Form):
    model_number = forms.IntegerField()
    equipment_name = forms.CharField()
    report_type = forms.CharField()

class QRdata(forms.Form):
    data = forms.CharField()


class EquipmentRemoved(forms.Form):
    equipment_name = forms.CharField()
    date_added = forms.DateField()
    date_removed = forms.DateField()
    remarks = forms.TextInput()
