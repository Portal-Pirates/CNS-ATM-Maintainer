from django import forms


class SearchForm(forms.Form):
    model_number = forms.IntegerField()
    equipment_name = forms.CharField()
    report_type = forms.CharField()

class QRdata(forms.Form):
    data = forms.CharField()
