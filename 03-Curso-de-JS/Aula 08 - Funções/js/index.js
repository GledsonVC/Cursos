/* FUNÇÕES
Uma função JavaScript é um bloco de código projetado para executar uma tarefa específica.

É como uma pequena "fábrica" onde você faz uma entrada e ele te dá uma saída.

Pode ser encarado como "Mini-programas" projetado para fazer uma tarefa que vai contribuir para todo código.

Uma função JavaScript é executada quando "algo" a invoca (chama-a).
*/

// FUNÇÃO SOMA
function soma(valor1, valor2) {
    return valor1 + valor2;
}

var total = soma(10, 23);
alert(total)

document.getElementById("texto").innerHTML = soma(10, 11);

function alertaHello() {
    alert("Olá pessoal.");
}

function paraCelsius(valorFahrenheit) {
    return (5 / 9) * (valorFahrenheit - 32);
}

alert("A temperatura é de " + paraCelsius(77) + " graus Celsius");
