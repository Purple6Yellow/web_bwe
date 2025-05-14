flatpickr(".datumpikker", {
    defaultDate: "today",
    minDate: "today",
    maxDate:"31.01.2027",
    altInput: true,
    enableTime: false,
    //dateFormat: "d-m-Y", 
    dateFormat: "d F Y", 
    locale: "nl", 
    AllowInput: true,
});


flatpickr(".tijdpikker",{
    enableTime: true,
    noCalendar: true,
    dateFormat: "H:i",
    defaultHour: 16,
    minTime: '8:00',
    maxTime:'23:00',
    time_24hr: true,
    minuteIncrement: 15,
});

//alert('datumprikker is geactiveerd')