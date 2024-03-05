from django import forms
from django.forms import ModelForm
from teretana.models import *

class OznakaForm(forms.ModelForm):
    class Meta:
        model = Oznaka
        fields = ['naziv']
        widgets = {'naziv': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Name' })}

class PlanForm(forms.ModelForm):
    oznake = forms.ModelMultipleChoiceField(queryset=Oznaka.objects.all(),
                                    to_field_name = 'naziv')
    class Meta:  
        model = Plan  
        fields = ['naziv', 'cijena', 'oznake']
        widgets = { 'naziv': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Name' }), 
            'cijena': forms.NumberInput(attrs={ 'class': 'form-control','placeholder':'Price' }),
            'oznake': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Select Tags'}),
        }
        labels={
            'oznake':'Select Tags',

        }

class TrenerForm(forms.ModelForm):
    class Meta:  
        model = Trener  
        fields = ['ime', 'image']
        widgets = { 'ime': forms.TextInput(attrs={ 'class': 'form-control','placeholder':'Name' }), 
            'image': forms.FileInput(attrs={ 'class': 'form-control','placeholder':'Image' }),
        }

class PretplatnikForm(forms.ModelForm):
    plan = forms.ModelChoiceField(queryset=Plan.objects.all(),
                                    to_field_name = 'naziv',
                                    empty_label="Select Plan")
    
    trener = forms.ModelChoiceField(queryset=Trener.objects.all(),
                                    to_field_name = 'ime',
                                    empty_label="Select Trainer")

    class Meta:
        model = Pretplatnik
        fields = ['trener', 'plan', 'datum_r', 'spol', 'adresa']
        GENDER_CHOICES = (
            ('', 'Select a Gender'),
            ('Female', 'Female'),
            ('Male', 'Male'),
        )
        widgets = {
            'trener':forms.TextInput(attrs={'class':'form-control','placeholder':'Select Trainer'}),
            'plan':forms.TextInput(attrs={'class':'form-control','placeholder':'Select Plan'}),
            'datum_r':forms.DateInput(attrs={'class':'form-control','placeholder':'Enter Date of Birth'}),
            'spol':forms.Select(choices=GENDER_CHOICES,attrs={'class': 'form-control'}),
            'adresa':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Address'}),
        }
        labels={
            'plan':'Select Plan',
            'trener':'Select Trainer',
            'datum_r':'Datum_r',

        }

    def __init__(self, *args, **kwargs):
        super(PretplatnikForm, self).__init__(*args, **kwargs)
        # Add first_name and last_name fields from the User model
        self.fields['first_name'] = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter First Name'}))
        self.fields['last_name'] = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Last Name'}))

    def save(self, commit=True):
        # Save the User instance first
        user = super(PretplatnikForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
        # Save the Pretplatnik instance
        pretplatnik = super(PretplatnikForm, self).save(commit=False)
        pretplatnik.korisnik = user
        if commit:
            pretplatnik.save()
        return pretplatnik