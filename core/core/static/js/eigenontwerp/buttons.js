$(document).ready( function() {

    $('#btn_programma').on('click', function URL(){
        location.href = "/formulier/programma.html"
        //console.log('buttonBK werkt')
        alert('Wilt u programma echt zien?')
    });
    
    $('#btn_reservering').on('click', function URL(){
        location.href = "/formulier/reservering.html"
        //console.log('reservering')
        alert('Wilt u Barthkapel huren?')
    });

    $('#btn_kunstenaars').on('click', function URL(){
    location.href = "/formulier/kunstenaars.html"
    //console.log('reservering')
    alert('Wilt u zien wie er gebruikt maakt van de ateliers?')
    });

    $('#btn_wachtlijst').on('click', function URL(){
    location.href = "/formulier/wachttlijst.html"
    //console.log('reservering')
    alert('Wilt u zich inschrijven voor de wachtlijst?')
    });

});