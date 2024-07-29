let section_abajo=document.getElementById("open");
let tabla=document.getElementById ("tabla_1");

section_abajo.addEventListener('click',toogleTable);

function toogleTable(){
    tabla.classList.toggle('tabla_open');
}