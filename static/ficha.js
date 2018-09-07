// PREENCHE A DATA DE HOJE

window.onload = function() {
    var today = new Date();
    var dd = today.getDate();
    var mm = today.getMonth()+1; //January is 0!
    var yyyy = today.getFullYear();

    if(dd<10){dd='0'+dd;}
    if(mm<10){mm='0'+mm;}
    var today = yyyy + '-' + mm + '-' + dd;

    document.getElementById("data").value = today;
}

// CALCULA O IMC

var imc = document.getElementById('imc');
imc.addEventListener('focus', calculaIMC);

function calculaIMC() {
    peso = document.getElementById('peso').value;
    altura = document.getElementById('altura').value;
    if (altura > 40 && altura < 250 && peso > 1 && peso < 299) {
        imc.value = (parseFloat(peso/(altura*altura/10000)).toFixed(2));
    }
}


