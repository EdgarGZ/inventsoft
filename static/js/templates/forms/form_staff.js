function ViewFormPurchases(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Compra</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form action="" class="form">
                                    <select name="" id="" placeholder="Producto">
                                        <option value="">-- Producto --</option>
                                    </select>
                                    <input type="text" placeholder="Cantidad">
                                    <input type="text" placeholder="Total:">
                                    <select name="" id="" placeholder="Cliente">
                                        <option value="">-- Proveedor --</option>
                                    </select>
                                    <select name="" id="" placeholder="Vendedor">
                                        <option value="">-- Comprador --</option>
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

function ViewFormSales(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Venta</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-4 col-form-container">
                            <div class="form-container">
                                <form action="" class="form">
                                    <select name="" id="" placeholder="Producto">
                                        <option value="">-- Producto --</option>
                                    </select>
                                    <input type="text" placeholder="Cantidad">
                                    <input type="text" placeholder="Total:">
                                    <select name="" id="" placeholder="Cliente">
                                        <option value="">-- Cliente --</option>
                                    </select>
                                    <select name="" id="" placeholder="Vendedor">
                                        <option value="">-- Vendedor --</option>
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

function ViewFormStock(){
    return `
        <div class="container-fluid main-container" id="main-container">
            <div class="row main-row-container">
                <div class="col-10 result-container">
                    <div class="result-title">
                        <h2>Registro Inventario</h2>
                    </div>
                    <div class="row row-form-container">
                        <div class="col-10 col-sm-8 col-lg-5 col-xl-3 col-form-container">
                            <div class="form-container">
                                <form action="" class="form">
                                    <select name="" id="" placeholder="Producto">
                                        <option value="">-- Producto --</option>
                                    </select>
                                    <input type="text" placeholder="Cantidad:">
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