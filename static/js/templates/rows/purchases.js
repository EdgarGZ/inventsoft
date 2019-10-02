function getPurchasesEmployeeData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td>${element.product}</td>
                <td>${element.amount}</td>
                <td>${element.provider}</td>
                <td>${element.total}</td>
                <td>${element.buyer}</td>
                <td>${element.purchase_date}</td>
            </tr>
    `}
    return this.rows;
}

function getPurchasesAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.id}</th>
                <td class="table-actions">
                    <a href="/form/form-purchases/" class="edit-row">
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
                <td>${element.provider}</td>
                <td>${element.total}</td>
                <td>${element.buyer}</td>
                <td>${element.purchase_date}</td>
            </tr>
    `}
    return this.rows;
}