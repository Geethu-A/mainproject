from django import forms
from app.models import *
class Productform(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'
class Contactform(forms.ModelForm):
    class Meta:
        model=Contact
        fields='__all__'        