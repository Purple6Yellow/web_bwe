from django.urls import path
from . import view
from .view import AtelOverzicht1, AtelOverzicht2, ProgTemplate1, ProgTemplate2,  DetailProg, WW_Lijst, RS_Aanvraag, FT_Aanvraag, succes_view, controle
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('Barthkapel.html', view.barthkapel),
# ALGEMEEN - DIVERS
path('',view.index),
path('algemeen/index.html',view.index),
path('algemeen/menu.html',view.menu),
path('divers/contact.html', view.contact),
path('divers/oversbwe.html', view.oversbwe),
path('divers/privestat.html', view.privestat),
# CC - PANDEN
path('cc/voorwaarden.html', view.voorwaarden),
path('cc/ccinrichting.html', view.inrichting, name = "Inrichting"),
path('panden/panden.html', view.panden, name = "Panden"),
path('panden/rembrandt.html', view.rembrandt),
path('panden/lepelstr.html', view.lepel),
path('panden/looijerstr.html', view.looij),
path('panden/brouwersgr.html', view.brouwer),
path('panden/prinsegr.html', view.prins),
path('panden/tuinhuis.html', view.tuinhuis),
# HULP
path('hulp/controle.html', view.controle, name = "controle"),

# FORMULIER 
path('prog/<int:pk>/', DetailProg.as_view(), name = 'Prog-Detail'),

path('formulier/wachtlijst.html/', view.WW_Lijst, name = 'Wachtlijst'),
path('formulier/reservering.html/', view.RS_Aanvraag, name = 'Reservering'),

path('formulier/factuur.html/', view.FT_Aanvraag, name = 'Factuur'),
#path('formulier/factuur.html/<int:bedrijfsnaam_id>/', views.FT_Aanvraag, name = 'Factuur'),

path('algemeen/index.html/', ProgTemplate1.as_view(), name = 'Programma_index'),
path('formulier/programma.html/', ProgTemplate2.as_view(), name = 'Programma'),
# ATELIERS / HUURDERS  #
path('formulier/ateliers.html/', AtelOverzicht1.as_view(), name = 'Atelier1'),
path('basis/index.html/', AtelOverzicht2.as_view(), name = 'Atelier2'),

#path('formulier/reservering.html/', AanvraagForm.as_view(), name = 'Add_Aanvraag'),
path('succes/', view.succes_view, name='succes_url'),

# VERWIJDEREN
#path('formulier/factuur.html/', views.FT_Aanvraag, name = 'Factuur'),
##path('factuurgegevens.html/', views.Add_Factuur, name='Add-Factuur'),
#path('formulier/reservering.html/', views.AanvraagForm, name = 'Add_Aanvraag'),
#path('formulier/factuur.html/', views.RS_2_Aanvraag, name = "Factuurgevens"),
# // VERWIJDEREN
]

if settings.DEBUG:
    urlpatterns += static (settings.MEDIA_URL, document_root  =settings.MEDIA_ROOT)
