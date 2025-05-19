from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse, get_object_or_404
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Atel, Prog, Reserve
from .forms import Form_WW, Form_RS, Form_FT
######## JSON Serialization_Image #########
from django.conf import settings
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.http import JsonResponse 
from PIL import Image
######## JSON Serialization_Image #########
######## mail verzenden #########
import smtplib
from email.mime.text import MIMEText
######## converteren #########
from datetime import datetime
###### NIET MEER NODIG???? #########
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from core.settings import EMAIL_HOST_USER
from django.contrib import messages
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
def privestat(request):
    return render (request, 'divers/privestat.html')
### // ALGEMEEN ###
### CC  ###
def voorwaarden(request):
    return render (request, 'cc/voorwaarden.html')
def inrichting(request):
    return render (request, 'cc/ccinrichting.html')
### // CC  ###
###  PANDEN ###
def voorwaarden(request):
    return render (request, 'cc/voorwaarden.html')
def panden(request):
    return render (request, 'panden/panden.html')
def rembrandt(request):
    return render (request, 'panden/rembrandt.html')
def lepel(request):
    return render (request, 'panden/lepelstr.html')
def looij(request):
    return render (request, 'panden/looijerstr.html')
def brouwer(request):
    return render (request, 'panden/brouwersgr.html')
def prins(request):
    return render (request, 'panden/prinsegr.html')
def tuinhuis(request):
    return render (request, 'panden/tuinhuis.html')

def barthkapel(request):
    return render (request, 'Barthkapel.html')
### //  PANDEN ###
###  HULP ###
def controle(request):
    return render (request, 'hulp/controle.html')
### // HULP ###

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


### PROGRAMMA #######
class ProgBlog(ListView):
    model = Prog

class ProgTemplate1(ProgBlog):
    def get_queryset(self):
        context = Prog.objects.all()[:1]
        return context
    
    template_name = 'algemeen/index.html'

class ProgTemplate2(ProgBlog):
    def get_queryset(self):
        context = Prog.objects.all()
        return context
       
    template_name = 'formulier/programma.html'

class DetailProg(DetailView):
    model = Prog
    template_name = 'formulier/programma_detail.html'

### // PROGRAMMA #######
### WACHTLIJST - INSCHRIJVING  ###
def WW_Lijst (request):
    # informatie # 
    onderwerp = "Inschrijving voor wachtlijst atelier ruimte"
    bericht = ""
    email_aanvrager = 'vikamper@hotmail.com'
    email_ontvanger = "stichtingbwe@gmail.com"
    app_password = 'ywhc koxx gxlt cghd'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    #// informatie # 
    submitted = False
    print('submitted is False')
    if request.method =="POST":
        print('check-wachtlijst')
        wlijst_form = Form_WW(request.POST) 
        if wlijst_form.is_valid():
            # Formulier is goed ingevuld
            wlijst_form.save() #opslaan in admin omgeving
            print('opgeslagen in admin omgeving')
            # email verzenden oa. info uit forms.py
            bericht = wlijst_form.wachtlijst_mail()
            msg = MIMEText(bericht)
            msg['Subject'] = onderwerp
            msg['From'] = email_aanvrager
            msg['To'] = email_ontvanger
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # TLS gebruiken
                server.login(email_ontvanger, app_password)
                server.sendmail(email_aanvrager, email_ontvanger, msg.as_string())
            print ('email reservering van ' +  email_aanvrager  + ' wordt verzonden!')
            #// email verzenden
            print('formulier is valide / goed ingevuld') 
        else:
            print('formulier niet valide, niet helemaal ingevuld')
        return HttpResponseRedirect('/formulier/wachtlijst.html?submitted=True')
    else:
        # print('pagina geopend, zonder te verzenden')
        wlijst_form = Form_WW() 
    submitted = 'submitted' in request.GET
    print('formulier is ingediend > dankbericht verschijnt')
    return render(request, 'formulier/wachtlijst.html', {'wlijst_form':  wlijst_form, 'submitted':submitted})
### // WACHTLIJST - INSCHRIJVING  ###
### RESERVERING - BK AANVRAAG  ###
def RS_Aanvraag (request):
    # informatie # 
    onderwerp = "Aanvraag Barthkapel verhuur"
    email_aanvrager = 'vikamper@hotmail.com'
    email_ontvanger = "infobarthkapel@gmail.com"
    app_password = 'pqhm grxp qdsq ujup' #naam app wachtwoord: reservering
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    #// informatie # 
    # KLIK OP VERZENDEN
    submitted = False
    if request.method =="POST":
        print('op button geklikt')
        res_form = Form_RS(request.POST) #info ophalen
        res_form.save() #opslaan in admin omgeving
        # FORMULIER GOED INGEVULD
        if res_form.is_valid():
            print('formulier is valide / goed ingevuld')
            print('is akkoord aangevinkt')
            # VOORWAARDEN GEACCEPT
            if res_form.cleaned_data.get('akkoord'):
                print('akkoord gegeven')
                pass
            else:
                print('geen akkoord gegeven')
                pass
            return 
            # VOORWAARDEN GEACCEPT
        else:
            pass
        return
        # // FORMULIER GOED INGEVULD
    else:
        print('niet op button geklikt')
        pass
    return render(request, 'formulier/reservering.html', {'res_form':  res_form, 'submitted':submitted})
    # // KLIK OP VERZENDEN
### // RESERVERING - BK AANVRAAG  ###

     


### HULP ###
def controle(request):
    data= request.session.get('opgehaaldeG', {})
    data2 = request.session.get('ophaal', {})
    return render(request, 'hulp/controle.html', {'data': data})
    
def succes_view(request):
    return HttpResponse("Je formulier is succesvol verzonden!")
### // HULP ###

def FT_Aanvraag(request):
    return HttpResponse("Je formulier is succesvol verzonden!")




