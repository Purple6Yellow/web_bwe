$(document).ready(function(){
    //console.log("pagina is geladen")
    $('#menu').on('click', function(event){
        //alert ('animate werkend- baseweb')
        event.stopPropagation();
        $('#menuMobiel').slideToggle();
    });
    $(document).click(function(){
        $('#menuMobiel').slideUp();
    });
    $('#menu').on('click', function(event){
        event.stopPropagation(); //Zorgt dat het niet sluit bij klikken op 
    })

});
