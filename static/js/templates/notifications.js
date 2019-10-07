function ZeroNotifications(){
    return `<h3 id="zero-notif">No hay notificaciones</h3>`;
}

function ViewNotifications(){
    return `
        <div class="container-fluid main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="far fa-clock"></i>
                        <h2>Historial<h2>
                    </div>
                    <div class="row records-container" id="records-container">

                        <div class="col-xl-3 col-lg-4 col-sm-6 col-12">
                            <div class="record">
                                <div class="details">
                                    <label>30/09/2019</label>
                                </div>
                                <div class="content">
                                    <p>Se agregó un producto en la tabla Productos </p>
                                </div>
                            </div>
                        </div>
                        
                    </div>
                </div>
            </div>
        </div>
    `
}