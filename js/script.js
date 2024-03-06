// alert("Hello World")
// console.log("Só quem é dev vai descobir")
// area de registro
// VAR
// LET
// CONST
// query=pesquisa, seletor
let nome = document.querySelector("#nome")

function exibirnome(){
    console.log(nome.value)
    if(nome.value == ""){
        nome.style.border = "2px solid red"
    }
    else{
        nome.style.border = "2px solid green"
    }
}

nome.addEventListener("blur",exibirnome)


let idade = document.querySelector("#idade");

idade.addEventListener("blur",function(){
    // Converter o valor da idade para um numero usando parserINT
    let idadeValor = parseInt(idade.value);
    
    if(idadeValor <= 18){
        alert("voce possui mais de 18 anos!")
    
    }   else    {
        alert("infelizmente, voce nao é de maior!");
    }   
});
let endereco = document.querySelector("#endereco");