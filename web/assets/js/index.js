let nav = document.querySelector("nav");
let headText = nav.querySelector(".head-text");

headText.addEventListener("click",()=>{
    if (nav.classList.contains("active")) {
        headText.innerHTML = "More";
    }else{
        headText.innerHTML = "Less";
    }
    nav.classList.toggle("active")
})

function closePopup(){
    nav.classList.remove("active");
    headText.innerHTML = "More";
}