function getProductsEmployeeData(data){
    this.rows = "";
    for(product of data){
        this.rows += `
        <tr>
            <th scope="row">${product.product_key}</th>
            <td>${product.name}</td>
            <td>${product.description}</td>
            <td>${product.price}</td>
            <td>${product.category}</td>
            <td>${product.provider}</td>
        </tr>
    `}
    return this.rows;
}

function getProductsAdminData(data){
    this.rows = "";
    for(product of data){
        this.rows += `
        <tr>
            <th scope="row">${product.product_key}</th>
            <td class="table-actions">
                <a href="/form/form-products/" class="edit-row">
                    <i class="fas fa-pen"></i>
                    <span>Editar</span>
                </a>
                <a href="">
                    <i class="fas fa-trash"></i>
                    <span>Borrar</span>
                </a>
            </td>
            <td>${product.name}</td>
            <td>${product.description}</td>
            <td>${product.price}</td>
            <td>${product.category}</td>
            <td>${product.provider}</td>
        </tr>
    `}
    return this.rows;
}