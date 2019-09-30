function ViewFormProduct(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Producto</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form action="" class="form">
                                    <input type="text" placeholder="Identificador:">
                                    <input type="text" placeholder="Nombre:">
                                    <textarea name="" id="" placeholder="Descripción..."></textarea>
                                    <input type="text" placeholder="Precio:">
                                    <select name="" id="" placeholder="Categoría">
                                        <option value="">-- Categoría --</option>
                                    </select>
                                    <select name="" id="" placeholder="Proveedor">
                                        <option value="">-- Proveedor --</option>
                                    </select>
                                    <button type="submit" class="btn btn-submit">Guardar</button>
                                    <a href="" class="btn secondary-btn">Cancelar</a>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    `;
}
