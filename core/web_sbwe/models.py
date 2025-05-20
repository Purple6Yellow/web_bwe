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
# INSCHRIJFFORMULIER / ATELIERS #
class Wacht(models.Model):
  voornaam = models.CharField('voornaam', max_length=50,  blank=False, null = True)
  achternaam = models.CharField('achternaam', max_length=50,  blank=False, null = True)
  email = models.EmailField('email',unique=False,   blank=False, null = True)
  telefoon = models.CharField('telefoon', max_length=30, blank = False, null = True)

  bedrijfsnaam = models.CharField('bedrijfsnaam', max_length=50, blank=False, null = True)
  kvk = models.IntegerField()

  werk = models.CharField(blank = True, null = True, max_length=20,)
  vierkantm = models.CharField(max_length = 5, blank =False, null = True, 
      choices =[('30m2', '30m2'), ('50m2','50m2'),('100m2','100m2'),('150m2','150m2'),])
  voorziening = models.CharField(blank = True, null = True, max_length=20,)
  delen = models.CharField(max_length = 20, blank =False, null = True, 
      choices =[('zelfstandig', 'zelfstandig'), ('delen','delen'),])
  startdatum = models.DateField(default=timezone.now, blank=False, null = True)
  website = models.URLField(blank = True, null = True)
  afbeelding = models.ImageField(upload_to='images/', null = True, blank = True)
  akkoord = models.BooleanField(default=False, null= False, blank = False)

  def publish(self):
    self.save()

  def __str__(self):
    return str(self.startdatum) + " - " + str(self.achternaam) + " (" + str(self.bedrijfsnaam)  +")"
# // INSCHRIJFFORMULIER / ATELIERS #
# AANVRAAGFORMULIER / CC    #
class Reserve(models.Model):
  bedrijfsnaam = models.CharField('Bedrijfsnaam', max_length=200, blank=True, null =False)
  naam = models.CharField('Voor & achternaam', max_length=200,  blank=False, null = False)
  email = models.EmailField('Email',  blank=False, null = True)
  datum = models.DateField(default=timezone.now, blank=False, null = False)
  starttijd = models.TimeField(default=timezone.now, blank=False, null = False)
  eindtijd = models.TimeField(default =timezone.now , blank=False, null = False) 
  akkoord = models.BooleanField(default=False, blank = False, null= False)
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
    return str(self.datum) + " - " + str(self.naam) + " (" + str(self.bedrijfsnaam)  +")"
# // AANVRAAGFORMULIER / CC #
# FACTUUR FORMULIER / CC    #
class Factuur(models.Model):
    bedrijfsnaam = models.CharField('Bedrijfsnaam', max_length=200, blank = True, null = True)
    naam = models.CharField('Voor & achternaam', max_length=200, blank=False, null = True)
    email = models.EmailField('Email', blank=False, null = True)   
    adres = models.CharField('Adres', max_length=80, blank=False, null = True)
    postcode = models.CharField('Postcode', max_length=20, blank=False, null = True)
 
    def __str__(self):
      # return self.bedrijfsnaam + ' | ' + self.naam + ' | '
      return self.bedrijfsnaam
# // FACTUUR FORMULIER / CC    #