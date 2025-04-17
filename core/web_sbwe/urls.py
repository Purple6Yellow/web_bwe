from django.urls import path
from . import views
from .views import AtelOverzicht1, AtelOverzicht2, ProgTemplate1, ProgTemplate2,  DetailProg, WW_Lijst, RS_Aanvraag, RS_2_Aanvraag
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('Barthkapel.html', views.barthkapel),
# ALGEMEEN - DIVERS
path('',views.index),
path('algemeen/index.html',views.index),
path('algemeen/menu.html',views.menu),
path('divers/contact.html', views.contact),
path('divers/oversbwe.html', views.oversbwe),
# CC - PANDEN
path('cc/voorwaarden.html', views.voorwaarden),
path('cc/ccinrichting.html', views.inrichting),
path('panden/panden.html', views.panden),
path('panden/rembrandt.html', views.rembrandt),
path('panden/lepelstr.html', views.lepel),
path('panden/looijerstr.html', views.looij),
path('panden/brouwersgr.html', views.brouwer),
path('panden/prinsegr.html', views.prins),
path('panden/tuinhuis.html', views.tuinhuis),

# FORMULIER 
path('prog/<int:pk>/', DetailProg.as_view(), name = 'Prog-Detail'),

path('formulier/wachtlijst.html/', views.WW_Lijst, name = 'Wachtlijst'),
path('formulier/reservering.html/', views.RS_Aanvraag, name = 'Reservering'),
path('formulier/factuur.html/', views.RS_2_Aanvraag, name = "Factuurgevens"),
path('algemeen/index.html/', ProgTemplate1.as_view(), name = 'Programma_index'),
path('formulier/programma.html/', ProgTemplate2.as_view(), name = 'Programma'),
# ATELIERS / HUURDERS  #
path('formulier/ateliers.html/', AtelOverzicht1.as_view(), name = 'Atelier1'),
path('basis/index.html/', AtelOverzicht2.as_view(), name = 'Atelier2'),

#path('formulier/reservering.html/', AanvraagForm.as_view(), name = 'Add_Aanvraag'),

##path('factuurgegevens.html/', views.Add_Factuur, name='Add-Factuur'),
#path('formulier/reservering.html/', views.AanvraagForm, name = 'Add_Aanvraag'),


]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root  =settings.MEDIA_ROOT)
