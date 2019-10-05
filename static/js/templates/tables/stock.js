function ViewEmployeeStockTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-cubes"></i>
                        <h2>Registros - Almacén</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn" onclick="navigate('/form/form-stock/')">Nuevo registro</button>
                        <button class="result-option other-option btn secondary-btn">Crear reporte</button>
                        <button class="result-option other-option btn secondary-btn">Descargar CSV</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Producto</th>
                                <th scope="col">Cantidad</th>
                            </thead>
                            <tbody>`;
                                this.template += getStockEmployeeData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

//<button class="result-option main-option btn" onclick="navigate('/form/form-stock/')">Nuevo registro</button>
function ViewAdminStockTable(data){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-cubes"></i>
                        <h2>Registros - Almacén</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option other-option btn secondary-btn">Crear reporte</button>
                        <button class="result-option other-option btn secondary-btn">Descargar CSV</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Acciones</th>
                                <th scope="col">Producto</th>
                                <th scope="col">Cantidad</th>
                            </thead>
                            <tbody>`;
                                this.template += getStockAdminData(data);
                                this.template += `</tbody>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}
    