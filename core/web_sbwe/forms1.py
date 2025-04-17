from django import forms
from django.forms import ModelForm
from .models import Inschrijf, Aanvraag

########## INSCHRIJFFORMULIER #############
class InschrijfForm (forms.ModelForm):
    class Meta:
        model = Inschrijf
        fields = '__all__'
        labels = {
            'bedrijfsnaam': '',
            'kvk': '',} 
        widgets = {
            'bedrijfsnaam':forms.TextInput(attrs={'class':'form-control rounded-3', 'placeholder':'optioneel', 'id': 'bedrijfsnaam',}),
            'kvk':forms.TextInput(attrs={'class':"form-control rounded", 'placeholder':'optioneel', 'id': 'kvk',}),
            'website':forms.TextInput(attrs={'class': "form-control rounded-5", "placeholder": "web adres of instagram adres", 'id': 'website', }),
        }
########## // INSCHRIJFFORMULIER ###########
########## AANVRAAGFORMULIER #############
class AanvraagForm(forms.ModelForm):
    class Meta:
        model = Aanvraag
        fields = '__all__'
        labels = {  
            'bedrijfsnaam':'',
            'naam':'',
            'email':'',
            'datum':'Datum',
            'starttijd':'Begintijd',
            'eindtijd':'Eindtijd',
            'gasten': '' ,
            'activiteit':'',
            'Nawnodig':'Heeft u al eerder gereserveerd?',
            'akkoord': 'Ik ga akkoord met de voorwaarden:',}
        widgets = {   
            'bedrijfsnaam':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Bedrijfsnaam', 'id': 'bedrijfsnaam',}),
            'naam':forms.TextInput(attrs={'class':'form-control', 'id': 'naam', 'placeholder':'Voor en Achternaam'}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'id':'email','placeholder':'Emailadres'}), 
            ##################
            'datum': forms.DateTimeInput(attrs={'id': 'datepicker', 'class': 'form-control', 'placeholder': 'datum'}),
            'starttijd': forms.DateTimeInput(attrs={'class': 'form-control, timepicker', 'id':'start_time', 'placeholder':'Selecteer starttijd'}),
            'eindtijd': forms.DateTimeInput(attrs={'class': 'form-control, timepicker', 'id':'end_time','placeholder':'Selecteer eindtijd'}),
            'message':forms.Textarea(attrs={'class':'form-control1', 'placeholder':'Toelichting / Beschrijving '}),
            'gasten':forms.Select(attrs={'class':'form-control', 'placeholder':'Voor hoeveel mensen organiseert u deze activiteit?'}),
            'activiteit':forms.Select(attrs={'class':'form-control','placeholder':'Hoeveel mensen zijn uitgenodigd'}),
            ##################
            'Nawnodig':forms.CheckboxInput(attrs = {'id': 'factuurgegevens', 'class': 'form-control2'}),
            'akkoord':forms.CheckboxInput(attrs = {'id': 'akkoord', 'class': 'form-check-input'}),
            ##################
            }

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.fields['akkoord'].required = True # zorgt ervoor dat dit verplicht is

def generate_message(self):
    """
    Genereert een dynamisch bericht gebaseerd op de ingevoerde gegevens.
    """
    naam = self.cleaned_data.get('naam', 'Klant')
    bedrijfsnaam = self.cleaned_data.get('bedrijfsnaam', 'onbekend')
    datum = self.cleaned_data.get('datum', 'onbekend')
    starttijd = self.cleaned_data.get('start_time', 'onbekend')
    eindtijd= self.cleaned_data.get('end_time', 'onbekend')
    gasten = self.cleaned_data.get('gasten', 'onbekend')
    email = self.cleaned_data.get('email_adres', 'onbekend')
    activiteit = self.cleaned_data.get('activiteit', 'onbekend')
    message = self.cleaned_data.get('message', 'onbekend')
    return (
        f"Hierbij de gegevens van mijn aanvraag.\n\n"

        f"Bedrijfsnaam: {bedrijfsnaam} t.a.v. {naam}\n"
        f"Datum: {datum} van {starttijd} tot {eindtijd}\n"
        f"Activiteit: {activiteit}.\n"
        f"Aantal genodigden: {gasten}\n"
        f"Beschrijving: {message}\n\n"

        f"Mijn gegevens.\n"
        f"Email: {email}\n"
        f".\n\n"
        f"Ik heb de voorwaarden van de Barthkapel gelezen en ga akkoord."
    )


 ########## AANVRAAGFORMULIER #############33