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

function showModal(text, location){
    document.body.innerHTML += `
        <div class="modal-back" id="modal-back">
            <div class="modal-container">
                <div class="modal-div">
                    <h3>${text}</h3>
                    <i class="fas fa-check-circle"></i>
                </div>
            </div>
        </div>
        `;         
    setTimeoutHTML('modal-back-show', 'modal-back', 1000);  
    if(location){ 
        setTimeout(function(){
            window.location.href = location;
        }, 1000)
    }
}