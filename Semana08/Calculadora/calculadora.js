//var valor = parseInt(0);
var valor;

function botao(num){
    valor = document.calc.visor.value += num;
    //valor += parseInt(num);
    //document.getElementById("visor").value = valor;
}

function reseta(){
    document.calc.visor.value = '';
}

function calcula(){
    resultado = eval(valor);
    document.calc.visor.value = resultado.toLocaleString('pt-');
}