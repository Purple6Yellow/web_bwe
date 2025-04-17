from django import forms
from django.forms import ModelForm
from .models import Wacht, Reserve

########## INSCHRIJFFORMULIER #############
class Form_WW (forms.ModelForm):
    class Meta:
        model = Wacht
        fields = '__all__'
        labels = {
            'bedrijfsnaam': '',
            'kvk': '',} 
        widgets = {
            'bedrijfsnaam':forms.TextInput(attrs={'class':'form-control rounded-3', 'placeholder':'optioneel', 'id': 'bedrijfsnaam',}),
            'kvk':forms.TextInput(attrs={'class':"form-control rounded", 'placeholder':'optioneel', 'id': 'kvk',}),
            'website':forms.TextInput(attrs={'class': "form-control rounded-5", "placeholder": "web adres of instagram adres", 'id': 'website', }),
        }

    def wachtlijst_mail(self):
        print('invulling van email is gereed')
        #invulling van email - verzonden via views.py
        bedrijfsnaam = self.cleaned_data.get('bedrijfsnaam','' )
        kvk = self.cleaned_data.get('kvk','niet van toepassing' )
        voornaam = self.cleaned_data.get('voornaam', 'Klant')
        achternaam = self.cleaned_data.get('achternaam', '')
        ####datum = self.cleaned_data.get('naam', 'Klant')
        email = self.cleaned_data.get('email', 'niet doorgegeven')
        telefoon = self.cleaned_data.get('telefoon', 'niet doorgegeven')
        werk = self.cleaned_data.get('werk', 'niet doorgegeven')
        vierkantem = self.cleaned_data.get('vierkantem', 'niet doorgegeven')
        voorziening = self.cleaned_data.get('voorziening', 'niet doorgegeven')
        delen = self.cleaned_data.get('delen', 'niet doorgegeven')
        ##startdatum = self.cleaned_data.get('startdatum', 'niet doorgegeven')
        website = self.cleaned_data.get('website', 'niet doorgegeven')
        return (
            f"Beste SBWE,\n"
            f"Via dit formulier laat ik weten graag op de wachtlijst voor een atelier ruimte te staan.\n"
            f"Dit zijn mijn gegevens:\n\n"
            f"Bedrijfsnaam: {bedrijfsnaam}\n"
            f"Kvk-nummer: {kvk}\n"
            f"Naam: {voornaam} {achternaam}\n"
            f"Mijn emailadres: {email}\n"
            f"Mijn telefoonnummer: {telefoon}\n\n"

            ###f"Datum: {datum} van {starttijd} tot {eindtijd}\n"
            f"Ik maak dit soort dingen: {werk}\n"
            f"Ik heb het volgende aantal m2 minimaal nodig: {vierkantem}\n"
            f"De volgende voorzieningen heb ik nodig: {voorziening}\n"
            f"Ik wil mijn atelier graag: {delen}\n"
            ##f"Ik zoek een ruimte per: {startdatum}\n"
            f"-----------------: {website}\n\n"
            f"Ik heb de voorwaarden ""privacy"" gelezen en ga akkoord."
        )
########## // INSCHRIJFFORMULIER ###########
########## AANVRAAGFORMULIER #############
class Form_RS(forms.ModelForm):
    class Meta:
        model = Reserve
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
            'Nawnodig':'',
            'akkoord': '',}
        
    def reservering_mail(self):
        print('invulling van email is gereed')
        #invulling van email - verzonden via views.py
        bedrijfsnaam = self.cleaned_data.get('bedrijfsnaam','niet van toepassing' )
        naam = self.cleaned_data.get('naam', 'Klant')
        ####datum = self.cleaned_data.get('naam', 'Klant')
        activiteit = self.cleaned_data.get('activiteit', 'niet doorgegeven')
        gasten = self.cleaned_data.get('gasten', 'niet doorgegeven')
        email = self.cleaned_data.get('email', 'niet doorgegeven')

        return (
            f"Beste SBWE, \n"
            f"Via het formulier op uw website stuur ik u mijn aanvraag voor het huren van de Barthkapel.\n\n"
            f"Bedrijfsnaam: {bedrijfsnaam}\n"
            f"Naam: {naam}\n"
            f"Mijn emailadres: {email}\n\n"

            ###f"Datum: {datum} van {starttijd} tot {eindtijd}\n"
            f"Activiteit: {activiteit}\n"
            f"Aantal genodigden: {gasten}\n\n"

            f"Ik heb de voorwaarden van de Barthkapel gelezen en ga akkoord."
            )

 





