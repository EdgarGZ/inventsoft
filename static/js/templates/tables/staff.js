function ViewAdminAreaStaffTable(){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-users"></i>
                        <h2>Registros - Personal</h2>
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
                                <th scope="col">Correo</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Apellido(s)</th>
                                <th scope="col">Fecha Inicio</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">AA001</th>
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
                                    <td>usuario@mail.com</td>
                                    <td>Jhon</td>
                                    <td>Doe</td>
                                    <td>29-06-2019</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}

function ViewSuperAdminStaffTable(){
    this.template = `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <i class="fas fa-users"></i>
                        <h2>Registros - Personal</h2>
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
                                <th scope="col">Correo</th>
                                <th scope="col">Nombre</th>
                                <th scope="col">Apellido(s)</th>
                                <th scope="col">Fecha Inicio</th>
                                <th scope="col">Area</th>
                                <th scope="col">Super Admin</th>
                                <th scope="col">Area Admin</th>
                                <th scope="col">Empleado</th>
                            </thead>
                            <tbody>
                                <tr>
                                    <th scope="row">AA001</th>
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
                                    <td>usuario@mail.com</td>
                                    <td>Jhon</td>
                                    <td>Doe</td>
                                    <td>29-06-2019</td>
                                    <td>AV</td>
                                    <td>false</td>
                                    <td>false</td>
                                    <td>true</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </div>
    `;
}