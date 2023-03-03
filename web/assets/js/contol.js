let table = document.querySelector("table");
let tbody = table.querySelector("tbody");
let form = document.querySelector(".form");

form.addEventListener("submit",(e)=>{
    e.preventDefault();

    sendLayerRequest()
})

function sendLayerRequest(){
    let xhr = createXHR();

    let formobj = new FormData(form);

    xhr.addEventListener("load",(e)=>{
        tbody.innerHTML = e.target.responseText;
    })

    xhr.open("POST","./orderRN");

    xhr.send(formobj);
}