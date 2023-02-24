from django import forms
from .models import Booking


class BookingForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields="__all__"

    def __init__(self,*args,**kwargs):
        super(). __init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs['class']='form-control'
            field.widget.attrs['placeholder']='Your '+field.label


#class registerationForm(forms.ModelForm):

    #class Meta:
        #model=registeration
        #fields="__all__"
        #widgets={'password':forms.PasswordInput()}

    #def __init__(self,*args,**kwargs):
        #super(). __init__(*args,**kwargs)
        #for field in self.fields.values():
           # field.widget.attrs['placeholder']='Your '+field.label
           # field.widget.attrs['class']='form-control'
           
           
