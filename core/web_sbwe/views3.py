from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.db import models
from django.views.generic import ListView, DetailView
from .models import Atel, Prog
from .forms import Form_WW, Form_RS
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
def lepel(request):
    return render (request, 'panden/lepelstr.html')


def barthkapel(request):
    return render (request, 'Barthkapel.html')
### // CC / PANDEN ###

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


### INSCHRIJFFORMULIER / WACHTLIJST  ###
def RS_Aanvraag (request):
    if request.method == "POST":
        print("check-reservering")
        res_form = Form_RS(request.POST)
        return render(request, 'formulier/reservering.html', {'res_form': res_form })
    else:
        return render(request, 'formulier/reservering.html')

def WW_Lijst (request):
    if request.method == "POST":
        print("check-wachtlijst")
        wlijst_form = Form_WW(request.POST)
        return render(request, 'formulier/wachtlijst.html', {'wlijst_form':  wlijst_form })
    else:
        return render(request, 'formulier/wachtlijst.html')

