let mapDiv = document.querySelector(".map");
let constDiv = document.querySelector(".constDiv");


(function getSimpleMap() {
    let xhr = createXHR();

    xhr.addEventListener("load",(e)=>{
        let msg = e.target.responseText;

        mapDiv.innerHTML = msg;

    })

    xhr.open("GET","http://127.0.0.1:5000/simplemap",true);

    xhr.send(null)
})()

//about formular
let form = document.querySelector(".form");

form.addEventListener("submit",(e)=>{
    e.preventDefault()

    sendFormQuery(form)
})
function sendFormQuery(form) {
    let xhr = createXHR();

    xhr.addEventListener("load",(e)=>{
        let msg = e.target.responseText;

        constDiv.innerHTML = msg;
        
        //closePopup()
    })

    let formObject = new FormData(form);

    xhr.open("POST","http://127.0.0.1:5000/constDetals",true);

    xhr.send(formObject)
}