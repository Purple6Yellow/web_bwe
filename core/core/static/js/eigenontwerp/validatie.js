document.getElementById('verzendknop').addEventListener('click', function() {
    // Hier komt de code die moet worden uitgevoerd wanneer op de knop wordt geklikt
    console.log('De verzendknop is geklikt!');
    alert('validatie.js is geactiveerd')
    alert('U heeft niet alles volledig ingevuld. ')

    const A = document.getElementById('naam').value;
    const B = document.getElementById('bedrijfsnaam').value;
    const C = document.getElementById('email').value;
    const D = document.getElementById('datepicker').value;
    const E = document.getElementById('start_time').value;
    const F = document.getElementById('end_time').value;
    const G = document.getElementById('akkoord')

    const vandaag = new Date();
    const jaar = vandaag.getFullYear();
    const maand = String(vandaag.getMonth()+1).padStart(2,'0'); // Maand is 0-gebaseerd, dus +1
    const dag = String(vandaag.getDate()).padStart(2,'0'); // Zorgt voor 2 cijfers, bijvoorbeeld '01'
    const vandaag1 =  (dag + "-" + maand + "-" + jaar )
    //alert (dag + "-" + maand + "-" + jaar )
    //alert (D)
    alert(vandaag1)

    //alert (A.length)
    if (A.length <= 3){
            alert('Uw naam is niet volledig geschreven')}
        else if (B.length <= 2){
            alert ('Graag uw bedrijfsnaam noteren')}
        else if (C.length <= 6){
            alert ('uw email is niet correct')}
        else if (D == vandaag1){
            alert('U heeft nog geen datum geselecteerd. U kunt voor vandaag niet reserveren')}
        else if (E.length == 0){
            alert('We hebben een starttijd nodig voordat we uw reservering kunnen beoordelen')}
        else if (F.length == 0) {
            alert("Uw eindtijd is niet bekend bij ons")}
        else if (!G.checked){
            //alert(!G.checked)
            // alert (G)
            event.preventDefault(); // Voorkom het indienen van het formulier
            alert("U moet akkoord gaan met de voorwaarden voordat u verder kunt gaan.")}
    });