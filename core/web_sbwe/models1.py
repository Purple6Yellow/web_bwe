from django.db import models
from django.utils import timezone
from PIL import Image

# ATELIERS / HUURDERS #
class Atel(models.Model):
  titel = models.CharField(max_length=200)
  tekst = models.TextField(blank = True, null = True, max_length=500)
  website = models.URLField(default = False, blank = True, null = True)
  afbeelding = models.ImageField(upload_to='images/', null = True, blank = True)

  def publish(self):
    self.datum = timezone.now()
    self.save()

  def __str__(self):
    return self.titel
# // ATELIERS / HUURDERS # 

# INSCHRIJFFORMULIER / ATELIERS #
class Inschrijf(models.Model):
  voornaam = models.CharField('voornaam', max_length=50,  blank=False, null = True)
  achternaam = models.CharField('achternaam', max_length=50,  blank=False, null = True)
  email = models.EmailField('email',unique=True,   blank=False, null = True)
  telefoon = models.CharField('telefoon', max_length=30, blank = False, null = True)

  bedrijfsnaam = models.CharField('bedrijfsnaam', max_length=50, blank=False, null = True)
  kvk = models.IntegerField()

  werk = models.CharField(blank = True, null = True, max_length=20,)
  vierkantem = models.CharField(max_length = 5, blank =False, null = True, 
      choices =[('30m2', '30m2'), ('50m2','50m2'),('100m2','100m2'),('150m2','150m2'),])
  voorziening = models.CharField(blank = True, null = True, max_length=20,)
  delen = models.CharField(max_length = 20, blank =False, null = True, 
      choices =[('zelfstandig', 'zelfstandig'), ('delen','delen'),])
  website = models.URLField(blank = True, null = True)
  afbeelding = models.ImageField(upload_to='images/', null = True, blank = True)
  akkoord = models.BooleanField(default=False)

  def publish(self):
    self.save()

  def __str__(self):
    return self.voornaam
# // INSCHRIJFFORMULIER / ATELIERS #


# AANVRAAGFORMULIER / CC    #
class Aanvraag(models.Model):
  bedrijfsnaam = models.CharField('Bedrijfsnaam', max_length=200, blank=False, null =False)
  naam = models.CharField('Voor & achternaam', max_length=200,  blank=False, null = False)
  email = models.EmailField('Email',  blank=False, null = True)
  datum = models.DateField(default=timezone.now, blank=False, null = True)
  starttijd = models.TimeField( blank=False, null = True)
  eindtijd = models.TimeField( blank=False, null = True) 
  akkoord = models.BooleanField(default=False)
  Nawnodig = models.BooleanField(default=False) 
  gasten = models.CharField(max_length=30,default = 'Onbekend',blank=False, null = True,
    choices=[
    ('1 tot 20 personen', '1-20'),
    ('20 tot 40 personen', '20-40'),
    ('40 tot 80 personen', '40-80'),])
  activiteit = models.CharField(max_length=40,default = 'Onbekend',blank=False, null = True,
    choices=[
    ('Concert', 'Concert'),
    ('Opname', 'Opname'),
    ('Les', 'Les'),
    ('Anders', 'Anders, geef toelichting'),])


  def __str__(self):
    return str(self.datum) + " / " + str(self.bedrijfsnaam)  + " t.a.v." + str(self.naam)
# // AANVRAAGFORMULIER / CC #

# PROGRAMMA BLOG   #
class Prog(models.Model):
  titel = models.CharField(max_length=200)
  datum = models.DateField(default=timezone.now)
  start = models.TimeField(blank = True, null = True)
  eind = models.TimeField(blank = True, null = True)
  website = models.URLField(default = False)
  image = models.ImageField(upload_to='images/', null = True, blank = True)
  image_name = models.CharField(max_length = 100, blank=True)

  def __str__(self):
    return f"{self.titel} -- {self.datum}"
  
  def publish(self):
    self.datum = timezone.now()
    self.save()
# //  PROGRAMMA BLOG #