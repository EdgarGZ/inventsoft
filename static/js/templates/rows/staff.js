function getStaffAdminAreaData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.emp_key}</th>
                <td class="table-actions">
                    <a href="/form/form-staff/" class="edit-row">
                        <i class="fas fa-pen"></i>
                        <span>Editar</span>
                    </a>
                    <a href="">
                        <i class="fas fa-trash"></i>
                        <span>Borrar</span>
                    </a>
                </td>
                <td>${element.email}</td>
                <td>${element.first_name}</td>
                <td>${element.last_name}</td>
                <td>${element.date_joined}</td>
            </tr>
    `}
    return this.rows;
}

function getStaffSuperAdminData(data){
    this.rows = "";
    for(element of data){
        this.rows += `
            <tr>
                <th scope="row">${element.emp_key}</th>
                <td class="table-actions">
                    <a href="/form/form-staff-admin/" class="edit-row">
                        <i class="fas fa-pen"></i>
                        <span>Editar</span>
                    </a>
                    <a href="">
                        <i class="fas fa-trash"></i>
                        <span>Borrar</span>
                    </a>
                </td>
                <td>${element.email}</td>
                <td>${element.first_name}</td>
                <td>${element.last_name}</td>
                <td>${element.date_joined}</td>
                <td>${element.area}</td>
                <td>${element.is_superuser}</td>
                <td>${element.is_areaadmin}</td>
                <td>${element.is_simplemortal}</td>
            </tr>
    `}
    return this.rows;
}