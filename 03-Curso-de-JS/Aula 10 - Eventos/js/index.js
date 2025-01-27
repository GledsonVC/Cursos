/* EVENTOS
Eventos são açõe disparadas pelas interação dos usuários na pagina 
Écomo correto manejo desse eventos que tornam as páginas interativas e dinâmica.

Existem muitos eventos. Veja os mais utilizados:

onclick => Disparado quando recebe um click
ondblclick => Disparado quando click duplo
onmouseover => Disparado quando o mouse está sobre o objeto
onmouseout => Disparado quando o mouse sai do objeto
onmousemove => Disparado quando o mouse é movido no elemento
onmousedown => Disparado quando o click do botão for pressionado
onmouseup = > Disparado quando o click do mouse é solto
onfocus => Disparado quando o elemento recebe o foco. Válido para input
onchange => Disparado quando há uma mudança no conteúdo. "Ao mudar"
onblur => Disparado quando o elemento perde o foco
onkeydown => Disparado quando uma tecla é pressionada 
onkeypress => Disparado quando uma tecla é pressionada e solta
onkeyup => Disparado quando uma tecla é solta sobre o elemento
onload => Disparado quando a página terminou de ser carregada. Body
onresize => Disparado quando há um redimencionamento da janela

*/

// ]ao dar um click no objeto ele muda o fundo para amarelo
function eventoClick() {
    document.body.style.background = "yellow";
}

// ao dar dois click sobre o objeto ele muda o fundo para vermelho
function eventoDblClick() {
    document.body.style.background = "red";
}

// passar mouse sobre o objeto muda o fundo para azul
function onMouseOver() {
    document.body.style.background = "blue";
}

// ao sair com o mouse do objeto ele muda o fundo para branco
function OnMouseMouseOut() {
    document.body.style.background = "white";
}

// ao mover o mouse ele escreverá " /Moveu o mouse!/ " e pulará uma linha no objeto
function onMouseMove() {
    let p = document.getElementById("moveMouseCriaParagrafo");
    p.append(" /Moveu o mouse!/ ");
}


// ao precionar o botão do mouse ele irá deixar a tela preta e letras brancas "
function onMouseDown() {
    document.body.style.background  = "black";
    document.body.style.color = "white";
}

// ao soltar o botão do mouse ele irá deixar a tela cinza e letras pretas "
function onMouseUp() {
    document.body.style.background  = "gray";
    document.body.style.color = "black";
}

