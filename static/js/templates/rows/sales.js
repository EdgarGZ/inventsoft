function getSalesEmployeeData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td>${element.product}</td>
                <td>${element.amount}</td>
                <td>${element.client}</td>
                <td>${element.total}</td>
                <td>${element.seller}</td>
                <td>${element.sale_date}</td>
            </tr>
    `}
    return this.rows;
}

function getSalesAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td class="table-actions">
                    <a href="/form/form-sales/" class="edit-row">
                        <i class="fas fa-pen"></i>
                        <span>Editar</span>
                    </a>
                    <a href="">
                        <i class="fas fa-trash"></i>
                        <span>Borrar</span>
                    </a>
                </td>
                <td>${element.product}</td>
                <td>${element.amount}</td>
                <td>${element.client}</td>
                <td>${element.total}</td>
                <td>${element.seller}</td>
                <td>${element.sale_date}</td>
            </tr>
    `}
    return this.rows;
}