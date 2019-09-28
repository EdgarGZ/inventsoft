function ViewEmployeeTable(){
    this.template = `
        <div class="row main-row-container">
            <div class="col-10 result-container">
                <div class="result-title">
                    <i class="fas fa-laptop"></i>
                    <h2>Categoría</h2>
                </div>
                <div class="table-responsive">
                    <table class="table table-container" id="table">
                        <thead>
                            <th scope="col">#</th>
                            <th scope="col">Apellido Paterno</th>
                            <th scope="col">Apellido Materno</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Correo</th>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row">1</th>
                                <td>León</td>
                                <td>Martínez</td>
                                <td>Alejandro</td>
                                <td>alejandro@gmail.com</td>
                            </tr>

                            <tr>
                                <th scope="row">2</th>
                                <td>León</td>
                                <td>Martínez</td>
                                <td>Alejandro</td>
                                <td>alejandro@gmail.com</td>
                            </tr>

                            <tr>
                                <th scope="row">3</th>
                                <td>León</td>
                                <td>Martínez</td>
                                <td>Alejandro</td>
                                <td>alejandro@gmail.com</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `; 
}

function ViewAdminTable(){
    this.template = `
        <div class="row main-row-container">
            <div class="col-10 result-container">
                <div class="result-title">
                    <i class="fas fa-laptop"></i>
                    <h2>Categoría</h2>
                </div>
                <div class="result-options-container">
                    <button class="result-option main-option btn">Nuevo registro</button>
                    <button class="result-option other-option btn secondary-btn">Crear reporte</button>
                </div>
                <div class="table-responsive">
                    <table class="table table-container" id="table">
                        <thead>
                            <th scope="col">#</th>
                            <th scope="col">Acciones</th>
                            <th scope="col">Apellido Paterno</th>
                            <th scope="col">Apellido Materno</th>
                            <th scope="col">Nombre</th>
                            <th scope="col">Correo</th>
                        </thead>
                        <tbody>
                            <tr>
                                <th scope="row">1</th>
                                <td class="table-actions">
                                    <a href="">
                                        <i class="fas fa-pen"></i>
                                    </a>
                                    <a href="">
                                        <i class="fas fa-trash"></i>
                                    </a>
                                </td>
                                <td>León</td>
                                <td>Martínez</td>
                                <td>Alejandro</td>
                                <td>alejandro@gmail.com</td>
                            </tr>

                            <tr>
                                <th scope="row">2</th>
                                <td class="table-actions">
                                    <a href="">
                                        <i class="fas fa-pen"></i>
                                    </a>
                                    <a href="">
                                        <i class="fas fa-trash"></i>
                                    </a>
                                </td>
                                <td>León</td>
                                <td>Martínez</td>
                                <td>Alejandro</td>
                                <td>alejandro@gmail.com</td>
                            </tr>

                            <tr>
                                <th scope="row">3</th>
                                <td class="table-actions">
                                    <a href="">
                                        <i class="fas fa-pen"></i>
                                    </a>
                                    <a href="">
                                        <i class="fas fa-trash"></i>
                                    </a>
                                </td>
                                <td>León</td>
                                <td>Martínez</td>
                                <td>Alejandro</td>
                                <td>alejandro@gmail.com</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `; 
}