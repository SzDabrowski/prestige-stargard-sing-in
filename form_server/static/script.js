const button1 = document.querySelector("header button");
const textobj = document.querySelector(".text-content");

button1.addEventListener('click', ()=>{textobj.scrollIntoView({behavior : "smooth"})})