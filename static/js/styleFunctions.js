function changeClass(styleClass, HTMLElement){
    document.getElementById(HTMLElement).classList.toggle(styleClass);
}

function setTimeoutHTML(styleClass, HTMLElement, duration){
    changeClass(styleClass, HTMLElement);
    setTimeout(function(){
        changeClass(styleClass, HTMLElement);
    }, duration);
}

function resetInputError(){
    const error = document.getElementById('error');
    if(error.innerHTML != ""){
        error.innerHTML = "";
    }
}