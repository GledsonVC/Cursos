/* Vamos entender Operadores:
-> Os operadores JavaScript são usados para atribuir valores, comparar valores, executar operações aritiméticas e muito mais.

São os sinais que usamos: + - * / = ++ -- += -+ && || etc...

São separados em 6 "categorias":
*/

// 1) Operadores Aritiméticos (matemáticos): + - * / 
// 2) Operadores de Atribuições: = ++ += -= *= /= -+
{
    var valor1, valor2, total;
    valor1 = 5;
    valor2 = 2;

    total = valor1 + valor2;
    alert("O soma de " + valor1 + " + " + valor2 + " = " + total);

    total = valor1 - valor2;
    alert("A subtração de " + valor1 + " - " + valor2 + " = " + total);

    total = valor1 * valor2;
    alert("A multiplicação de " + valor1 + " * " + valor2 + " = " + total);

    total = valor1 / valor2;
    alert("A divisão de " + valor1 + " / " + valor2 + " = " + total);

    total = ++valor1;
    alert("Essa expressão 'total = ++valor1'");
    alert("Faz com que o total atribua o valor do valor1 que era 5 + 1 = " + total);
    alert("E o valor1 que era 5 fique atribuindo ao 5 + 1 = " + valor1);

    total = --valor1;
    alert("Essa expressão 'total = --valor1'");
    alert("Faz com que o total atribua o valor do valor1 que era 6 - 1 = " + total);
    alert("E o valor1 que era 6 fique atribuindo ao 6 - 1 = " + valor1);

    valor1 += valor1;
    alert("Essa expressão 'valor1 += valor1'");
    alert("Faz com que o valor1 que é 5  receba ele mesmo mais o valor1 = " + valor1);

    valor1 -= valor1;
    alert("Essa expressão 'valor1 -= valor1'");
    alert("Faz com que o valor1 que é 6  receba ele mesmo menos o valor1 = " + valor1);
    // tbm funcionaria se utilizasse *= ou /=
}

// 3) Operadores de Sequência: +
{
    var nome, sobrenome, nome_completo;
    nome = "Gledsson ";
    sobrenome = "V Cavalheiro";
    nome_completo = nome + sobrenome
    alert(nome_completo)
}

// 4) Operadores de Comparação: == === !== < <= > >=
{
    var valor1, valor2, valor3, total;
    valor1 = 1;
    valor2 = "1";
    valor3 = 0
    total = (valor1 == valor2); // true (verdadeiro) ou false (falso)
    alert("valor1 = " + valor1 + ", valor2 = '" + valor2 + "'" + ", valor3 = " + valor3);
    alert("valor1 == valor2 = " + total);
    // === verifica o tipo e se os valores são iguais
    alert("valor1 === valor2 = " + (valor1 === valor2));
    alert("valor1 == valor3 = " + (valor1 == valor3));
    alert("valor1 === valor3 = " + (valor1 === valor3));
    alert("valor1 != valor2 = " + (valor1 != valor2));
    alert("valor1 != valor3 = " + (valor1 != valor3));
    //  !== verifica o tipo e se os valores são diferentes
    // < <= > >= funciona como todas outras programações
}


// 5) Operador Condicional (Ternário):
{
    var idade, eleitor;
    idade = 16;
    eleitor = (idade < 16) ? "Não, eleitor! " : "Sim, eleitor! ";
    alert("A resposta é: " + eleitor + " Ele tem " + idade + " anos");

    idade = 15;
    eleitor = (idade < 16) ? "Não, eleitor! " : "Sim, eleitor! ";
    alert("A resposta é: " + eleitor + " Ele tem " + idade + " anos");
}

// 6) Operadores Lógicos && || !(condição logica sendo negada)
{
    var idade, eleitor, deve_votar;
    idade = 16;
    deve_votar = ((idade >= 18) && (idade <= 70)) ? ", é obrigado a votar." : ", não é obrigado a votar."
    eleitor = (idade < 16) ? "Não, eleitor! " : "Sim, eleitor! ";
    alert("A resposta é: " + eleitor + " Ele tem " + idade + " anos" + deve_votar);
}
