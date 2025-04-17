from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Atel, Inschrijf, Prog
from .forms1 import AanvraagForm, InschrijfForm
######## JSON Serialization_Image #########
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse 
from PIL import Image
######## JSON Serialization_Image #########
######## mail verzenden #########
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from core.settings import EMAIL_HOST_USER
######## mail verzenden #########


### ALGEMEEN / DIVERS ###
def index(request):
    return render(request, 'algemeen/index.html')

def menu(request):
    return render(request, 'algemeen/menu.html')

def contact(request):
    return render (request, 'divers/contact.html')

def oversbwe(request):
    return render (request, 'divers/oversbwe.html')
### // ALGEMEEN ###

### CC / PANDEN ###
def reservering(request):
    return render (request, 'cc/reservering.html')
def voorwaarden(request):
    return render (request, 'cc/voorwaarden.html')
def panden(request):
    return render (request, 'panden/panden.html')
def rembrandt(request):
    return render (request, 'panden/rembrandt.html')

def barthkapel(request):
    return render (request, 'Barthkapel.html')



### ATELIERS  / HUURDERS ###
class Ateliers (ListView):
    model = Atel
    def get_queryset(self):
        queryset = Atel.objects.all()
        print (queryset)
        return queryset

class AtelOverzicht1(Ateliers):
    template_name = 'formulier/ateliers.html'

class AtelOverzicht2(Ateliers):
    template_name = 'algemeen/index.html'

### ATELIERS  / HUURDERS ###

### PROGRAMMA BLOG   ###
class ProgBlog(ListView):
    model: Prog
    #print('programma blog')
    def get_queryset(self):
        data = Prog.objects.all()
        return data
  
class ProgBlog1(ProgBlog):
  template_name = 'formulier/programma.html'

class ProgBlog2(ProgBlog):
    template_name = 'algemeen/index.html'
    #data = Prog.objects.order_by('datum')[:1]

class DetailProg(DetailView):
    model =  Prog
    template_name = 'formulier/programma_detail.html'

### // PROGRAMMA BLOG ###


### INSCHRIJFFORMULIER / WACHTLIJST  ###
def Wachtlijst (request):
    form = InschrijfForm
    if request.method == "POST":
        form = InschrijfForm
        print('check')
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('formulier/wachtlijst.html', pk=post.pk)
        else:
           form = InschrijfForm()   
    return render (request, 'formulier/wachtlijst.html', {'form': form})
### // INSCHRIJFFORMULIER ###

### AANVRAAGFORMULIER   ###
def Add_Aanvraag(request):
    print('aanvraagformulier actief')
    submitted = False
    if request.method == 'POST':
        aanvraag_form = AanvraagForm(request.POST, request.FILES)
        if aanvraag_form.is_valid():
            image_instance = aanvraag_form.save() # Als je een ModelForm gebruikt  
            image_url = settings.MEDIA_URL + str(image_instance.foto)
            ######### mail verzenden ############ 
            message = aanvraag_form .generate_message()
            subject = "Aanvraag Barthkapel huur"
            email1 = aanvraag_form.cleaned_data['email']
            email2 = 'infobarthkapel@gmail.com' # adres tbv aanvragen
            recipient_list=[email2]
            send_mail(  
            subject,
            message,
            EMAIL_HOST_USER, 
            recipient_list, 
            fail_silently=True )
            ######### // mail verzenden ############ 
            ######### nw formulier openen > ivm factuur adres  ############ 
            if aanvraag_form.cleaned_data.get('Nawnodig') =="ja":
                print('Specifiek factuuradres laten invullen')
                if request.method == "POST" and request.FILES.get("file"):
                    uploaded_file = request.FILES["file"] # temporary UploadedFile
                    file_data={ 
                    "name": uploaded_file,
                    "size": uploaded_file.size,
                    "content_type":uploaded_file.content_type,}        
                    ######### nw formulier openen > ivm factuur adres  ############ 
                    ######### // datum converteren ############ 
                    form_data = aanvraag_form.cleaned_data
                    if 'datum' in form_data:
                        form_data['datum'] = form_data['datum'].isoformat()
                        form_data['starttijd'] = form_data['starttijd'].isoformat()
                        form_data['eindtijd'] = form_data['eindtijd'].isoformat()
                        request.session['form_a_data'] = form_data
                        print("Ingevulde data set:", request.session['form_a_data'])
                        print(image_url)
                        ######### // datum converteren ############ 
                    return redirect('Add-Factuur') 
            else:
                print('aanvraag is gelukt')
                return HttpResponseRedirect('/formulier/reservering.html?submitted=True')
        else: 
            print("Aanvraag is niet valide")
    else:
        aanvraag_form = AanvraagForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request, 'reservering.html', {'aanvraag_form':aanvraag_form, 'submitted' : submitted})
### //AANVRAAGFORMULIER ###


### INSCHRIJFFORMULIER / WACHTLIJST  ###
def RS_Aanvraag (request):
    # informatie # 
    onderwerp = "Aanvraag Barthkapel verhuur"
    bericht = "Via het formulier op uw website stuur ik u mijn aanvraag voor het huren van de Barthkapel"
    email_aanvrager = 'vikamper@hotmail.com'
    email_ontvanger = "infobarthkapel@gmail.com"
    app_password = 'pbwh cuau qylx kjbn'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    #// informatie # 
    submitted = False
    print('submitted is False')
    if request.method == "POST":
        print("check-reservering")
        res_form = Form_RS(request.POST)
        if res_form.is_valid(): 
            #   formulier is goed ingevuld
            print('valide')
            #   formulier verzenden via mail:
            msg = MIMEText(bericht)
            msg['Subject'] = onderwerp
            msg['From'] = email_aanvrager
            msg['To'] = email_ontvanger
            print ('email reservering van' +  email_aanvrager  + 'wordt verzonden!')
            # Verbinden en verzenden
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # TLS gebruiken
                server.login(email_ontvanger, app_password)
                server.sendmail(email_aanvrager, email_ontvanger, msg.as_string())
            #// formulier verzenden via mail
            cleaned_data = res_form.cleaned_data
            res_form.save()
            #// formulier is goed ingevuld
            if res_form.cleaned_data.get('Nawnodig') ==True:
                print('Nawnodig = ja')
        else:
            print('niet valide')
            print(res_form.errors)
            return render(request, 'formulier/reservering.html', {'res_form':  res_form})
    else:
        print('op pagina - zonder verzending')
        res_form = Form_RS() 
        if 'submitted' in request.GET:
            submitted = True
            print('submitted is True')
            return render(request, 'formulier/reservering.html', {'res_form': res_form, 'submitted':submitted })
        return render(request, 'formulier/reservering.html', {'res_form': res_form, 'submitted':submitted })
### INSCHRIJFFORMULIER  ###

if 'submitted' in request.GET:
        submitted = True
else:
    print('formulier is niet ingediend > dankbericht verschijnt niet')

          
