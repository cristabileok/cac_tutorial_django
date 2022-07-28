from django import forms

class ContactInfo(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone = forms.IntegerField()
    msj = forms.CharField()    