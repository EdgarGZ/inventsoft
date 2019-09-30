function ViewEmployeePurchasesTable(){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-store"></i>
                        <h2>Registros - Compras</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option other-option btn secondary-btn">Crear reporte</button>
                        <button class="result-option other-option btn secondary-btn">Descargar CSV</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Producto</th>
                                <th scope="col">Cantidad</th>
                                <th scope="col">Cliente</th>
                                <th scope="col">Total</th>
                                <th scope="col">Comprador</th>
                                <th scope="col">Fecha Compra</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">1</th>
                                    <td>Producto 1</td>
                                    <td>100</td>
                                    <td>Jhon Doe</td>
                                    <td>500.00</td>
                                    <td>Sara James</td>
                                    <td>19-09-2019</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewAdminPurchasesTable(){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-store"></i>
                        <h2>Registros - Compras</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option main-option btn">Nuevo registro</button>
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
                                <th scope="col">Cliente</th>
                                <th scope="col">Total</th>
                                <th scope="col">Comprador</th>
                                <th scope="col">Fecha Compra</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">1</th>
                                    <td class="table-actions">
                                        <a href="" class="edit-row">
                                            <i class="fas fa-pen"></i>
                                            <span>Editar</span>
                                        </a>
                                        <a href="">
                                            <i class="fas fa-trash"></i>
                                            <span>Borrar</span>
                                        </a>
                                    </td>
                                    <td>Producto 1</td>
                                    <td>100</td>
                                    <td>Jhon Doe</td>
                                    <td>500.00</td>
                                    <td>Sara James</td>
                                    <td>19-09-2019</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}