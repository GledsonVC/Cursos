/* Vamos entender Variáveis
Variaveis são "recipientes" onde podemos armazenar informações que
podem vairar, ou seja, podem ter qualquer tipo de valor.

Noj Javascript temos 3 palavras-chaves para declarar variáveis:
-> var -> variavel que pode ser alterada com os valores

-> let -> variável que não pode ser redeclarada com outro valor 
    a não ser que seja dentro de um escopo {}

    -> const -> é uma variavel constante que nunca se pode alterar os valores mesmo que em escopo {} não é alterado o valor
*/

// Declação de variaveis
var pote = "Bombom";
alert(pote);

// Forma de declaração uma a uma
{
    var a = 2;
    var b = 3;
    var c = a + b;
    alert(c);
}

// Forma mais correta de declaração e atribuição
// Declaraçãode variaveis
var a, b, c;
// Atribuição de variáveis
a = 2;
b = 3;
c = a + b;
alert(c);

const nome = "Gledson";
const sobrenome = "Vasconcellos Cavalheiro";
const nome_completo = nome + " " + sobrenome;
document.getElementById("texto1").innerHTML =
    (nome_completo);



// Resultado: "42 Gledson" aqui irá somar a variavel idade + 1
{
    var idade, pessoa;
    idade = 41;
    pessoa = idade + 1 + " " + nome;
    document.getElementById("texto2").innerHTML =
        (pessoa);
}

// Resultado: "Gledson 411" aqui irá entender como texto e concatenar variavel idade e 1
{
    var pessoa2 = nome + " " + idade + 1;
    document.getElementById("texto3").innerHTML =
        (pessoa2);
}