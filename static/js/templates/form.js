function ViewEmployeeForm(){
    this.template = `
        <div class="row main-row-container">
            <div class="col-10 col-sm-6 col-lg-4 col-xl-4 result-container">
                <div class="result-title">
                    <h3>No tienes los permisos para esta acción.</h3>
                </div>
            </div>
        </div>
    `;
}

function ViewAdminForm(){
    this.template = `
        <div class="row main-row-container">
            <div class="col-10 col-sm-6 col-lg-4 col-xl-4 result-container">
                <div class="result-title">
                    <h2>Formulario Categoría</h2>
                </div>
                <div class="row row-form-container">
                    <div class="col-10 col-sm-10 col-lg-10 col-xl-8 col-form-container">
                        <div class="form-container">
                            <form action="" class="form">
                                <input type="text" placeholder="Nombre:">
                                <input type="text" placeholder="Apellido Paterno:">
                                <input type="text" placeholder="Apellido Materno:">
                                <input type="text" placeholder="Correo:">
                                <button type="submit" class="btn btn-submit">Guardar</button>
                                <a href="" class="btn secondary-btn">Cancelar</a>
                            </form>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}