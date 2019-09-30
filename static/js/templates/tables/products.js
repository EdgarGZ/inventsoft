function ViewEmployeeProductsTable(){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-box-open"></i>
                        <h2>Registros - Productos</h2>
                    </div>
                    <div class="result-options-container">
                        <button class="result-option other-option btn secondary-btn">Crear reporte</button>
                        <button class="result-option other-option btn secondary-btn">Descargar CSV</button>
                    </div>
                    <div class="table-responsive">
                        <table class="table table-container" id="table">
                            <thead>
                                <th scope="col">Id</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Precio</th>
                                <th scope="col">Categoría</th>
                                <th scope="col">Proveedor</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">PROD001</th>
                                    <td>Producto 1</td>
                                    <td>Caja con 10P</td>
                                    <td>500.00</td>
                                    <td>PAPA</td>
                                    <td>SABRITAS</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewAdminProductsTable(){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-box-open"></i>
                        <h2>Registros - Productos</h2>
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
                                <th scope="col">Nombre</th>
                                <th scope="col">Descripción</th>
                                <th scope="col">Precio</th>
                                <th scope="col">Categoría</th>
                                <th scope="col">Proveedor</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">PROD001</th>
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
                                    <td>Caja con 10P</td>
                                    <td>500.00</td>
                                    <td>PAPA</td>
                                    <td>SABRITAS</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}