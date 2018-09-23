M.AutoInit();

// PREENCHE A DATA DE HOJE

//window.onload = function() {
//    var today = new Date();
//    var dd = today.getDate();
//    var mm = today.getMonth()+1; //January is 0!
//    var yyyy = today.getFullYear();
//
//    if(dd<10){dd='0'+dd;}
//    if(mm<10){mm='0'+mm;}
//    var today = yyyy + '-' + mm + '-' + dd;
//
//    document.getElementById("data").value = today;
//}

// CALCULA OS PESOS
var pesoInput = document.getElementById('peso');
var alturaInput = document.getElementById('altura');
pesoInput.addEventListener('focusout', calculaPesos);
alturaInput.addEventListener('focusout', calculaPesos);


function calculaIMC() {
    imc.value = (parseFloat(peso/(altura*altura/10000)).toFixed(1));
};

function calculaIdeal() {
    if (homem){
        ideal.value = (altura - 100);
    }else if (mulher){
        ideal.value = (altura - 105);
    }else{
        ideal.value = (altura - 103);
    };
};

function calculaAjustado() {
    ajustado.value = (parseFloat(ideal.value) + (0.4*(peso - ideal.value))).toFixed(1);
};

function calculaPredito() {
    if (homem){
        predito.value = (50 + 0.91*(altura-152.4)).toFixed(1);
    }else if (mulher){
        predito.value = (45.5 + 0.91*(altura-152.4)).toFixed(1);
    }else{
        predito.value = (58 + 0.91*(altura-152.4)).toFixed(1);
    };
};

function calculaPesos(){
    peso = parseFloat(document.getElementById('peso').value);
    altura = parseFloat(document.getElementById('altura').value);
    homem = document.getElementById('masc').checked;
    mulher = document.getElementById('fem').checked;

    if (altura > 50 && altura < 230 && peso > 1 && peso < 299) {
        calculaIMC();
        calculaIdeal();
        calculaAjustado();
        calculaPredito();
    };
}

// MOSTRA COMPLEMENTO DAS PERGUNTAS
// Procedimentos Prévios
bool_previo.addEventListener('change', mostraPrevios);

function mostraPrevios(){
    if(bool_previo.checked){
        proc_previo.classList.remove('hide');
        adverso_b.classList.remove('hide');
    }else{
        proc_previo.classList.add('hide');
        adverso_b.classList.add('hide');
        adverso_i.classList.add('hide');
        bool_adverso.checked = false;
    }
}
window.onload = mostraPrevios();

// Eventos Adversos
bool_adverso.addEventListener('change', mostraAdversos);

function mostraAdversos(){
    if(bool_adverso.checked){
        adverso_i.classList.remove('hide');
    }else{
        adverso_i.classList.add('hide');
    }
}
window.onload = mostraAdversos();

// Alergias
bool_alergias.addEventListener('change', mostraAlergias);

function mostraAlergias(){
    if(bool_alergias.checked){
        alergias_i.classList.remove('hide');
    }else{
        alergias_i.classList.add('hide');
    }
}
window.onload = mostraAlergias();