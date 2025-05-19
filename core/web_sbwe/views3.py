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
    submitted = False
    VWaarde = False
    if request.method =="POST":
        print('check-reservering')
        res_form = Form_RS(request.POST)
        res_form.save() #opslaan in admin omgeving
        if res_form.is_valid():
            # Formulier is goed ingevuld
            print('formulier is valide / goed ingevuld')
            # // nodig voor (auto) invullen factuur formulier 
            # VOORWAARDEN GEACCEPT
            if res_form.cleaned_data.get('akkoord'):
                print('akkoord gegeven')
                # Converteer datum naar string (indien aanwezig)
                ophaal = res_form.cleaned_data
                if 'datum' in ophaal:
                    ophaal['datum'] = ophaal['datum'].isoformat()
                    ophaal['starttijd'] = ophaal['starttijd'].isoformat()
                    ophaal['eindtijd'] = ophaal['eindtijd'].isoformat()
                # // Converteer datum naar string (indien aanwezig)
                   # PAGINA LEZEN (GEGEVENS NIET VERLOREN)
                   
                # nodig voor (auto) invullen factuur formulier 
                request.session['opgehaaldeG'] = ophaal #opslaan
                print("Ingevulde data set:", request.session['opgehaaldeG'])
                # testen omdat database wel wordt opgeslagen, maar niet wordt opgehaald 
                print("uitgelezen", initial_data)
                print("SESSION KEY_RS_Aanvraag:", request.session.session_key) 
                request.session.modified = True
                request.session.save()
                # // testen omdat database wel wordt opgeslagen, maar niet wordt opgehaald 
                # email verzenden oa. info uit forms.py
                bericht = res_form.reservering_mail()
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
                # FACTUUR GEGEVENS
                if res_form.cleaned_data.get('Nawnodig'):
                    print('Ander formulier wordt geopend - factuur')
                    fac_form=Form_FT()
                    #return render(request, 'formulier/factuur.html', {'fac_form':  fac_form})  
                    #return redirect ('Factuur') # via urls.py openen van ander view
                    return redirect('factuur')
                else:
                    res_form = Form_RS(initial = initial_data)
                    print('Pagina factuur.html niet nodig')
                    #return HttpResponseRedirect('/formulier/reservering.html?submitted=True')
                return render(request, '/formulier/reserverings.html', {'res_form', res_form})
                # // FACTUUR GEGEVENS
            else:
                print ('geen akkoord')
                VWaarde = True
                print('VWaarde = True: Popup dat de voorwaarden niet zijn geaccepteerd')
                #return HttpResponseRedirect('/formulier/reservering.html')
            # // VOORWAARDEN GEACCEPT
        else:
            print('formulier niet valide, niet helemaal ingevuld')
            print ('pagina vernieuwd')
            ophaal = res_form.cleaned_data
            initial_data = request.session.get('opgehaald')#uitlezen
        return HttpResponseRedirect('/formulier/reservering.html?submitted=True')
    else:
        print('pagina geopend, zonder een verzoek')
        res_form = Form_RS() 
    submitted = 'submitted' in request.GET
    print('formulier is ingediend > dankbericht verschijnt')
    return render(request, 'formulier/reservering.html', {'res_form':  res_form, 'submitted':submitted})
### // RESERVERING - BK AANVRAAG  ###

###    FACTUUR - VERVOLG RESERVERING  ###
def FT_Aanvraag(request):
    OpgehaaldeG = request.session.get('OpgehaaldeG', {}) # Haal gegevens uit de sessie. Is in reservering opgeslagen
    # testen omdat database wel wordt opgeslagen, maar niet wordt opgehaald 
    request.session['OpgehaaldeG'] = OpgehaaldeG
    print("SESSION KEY_FT_Aanvraag:", request.session.session_key)
    # testen omdat database wel wordt opgeslagen, maar niet wordt opgehaald 
    print('Opgehaalde gegevens zijn: ')
    print(OpgehaaldeG)
    if 'datum' in OpgehaaldeG:
        OpgehaaldeG['datum'] = datetime.fromisoformat(OpgehaaldeG['datum']).date()
    if request.method == 'POST':
        print('check-factuurgegevens')
        fac_form = Form_FT(request.POST)
        if fac_form.is_valid():
            fac_form.save()
            return HttpResponseRedirect('/formulier/reservering.html?submitted=True')
        else:
            print('formulier error = ')
            print(fac_form.errors)
    else:
        print('Pagina opgeladen, niet verzonden')
        fac_form = Form_FT(initial = OpgehaaldeG)
        context = {'fac_form': fac_form}
    return render(request, '/formulier/factuur.html', context)
###  //  FACTUUR - VERVOLG RESERVERING  ###


############## VERWIJDEREN
###    FACTUUR - VERVOLG RESERVERING  ###
def FT_Aanvraag2(request, bedrijfsnaam_id):
    persoon = get_object_or_404(Reserve, pk = bedrijfsnaam_id)
    if request.method == 'POST':
        fac_form = Form_RS(request.POST, instance=persoon)
        fac_form.save()
        return redirect('klaar')
    else:
        fac_form = Form_RS(instance=persoon)
    return render(request, 'formulier/factuur.html', {'fac_form':  fac_form })
    # informatie / ophalen # 
    email = request.POST.get('email')
    fac_form = Reserve.objects.filter(email = email )
    #fac_form = Form_RS(instance=klant)
    
### // FACTUUR - VERVOLG RESERVERING  ###
### // RS2 - FACTUUR  ###




### // RS2 - FACTUUR  ###
def RS_2_Aanvraag(request):
    return render (request, 'formulier/factuur.html')

