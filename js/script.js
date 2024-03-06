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
// o addEventListener cria um evento para algum elemento, no caso estamos utilizando o evento "blur", que é qaundo o foco sai de um campo.

// nome.addEventListener("focus", function(){
//     nome.value = "Este campo não deve ficar vazio"
// })
let idade = document.querySelector("#idade")

idade.addEventListener("blur",function(){
    if(idade >= 18){
        alert("voce possui mais de 18 anos!")
    }
    else
    alert("infelizmente, voce nao é de maior!")
    
})
let endereco = document.querySelector()