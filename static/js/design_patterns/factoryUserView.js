function ViewError(){
    // this.template = "<h3>Error: User type invalid</h3>";
    window.location.href = '/logout/';
}

function UserViewFactory(ViewSuperAdmin, ViewAreaAdmin, ViewEmployee){
    this.create = (type) =>{        
        if (type === 0) return ViewSuperAdmin;
        if (type === 1) return ViewAreaAdmin;
        if (type === 2) return ViewEmployee;
        if (type != 0 && type != 1 && type != 2) return new ViewError();
    }
}

function FormViewFactory(){
    this.create = (area) =>{
        if(area === 'AAVEN') return ViewFormSales();
        if(area === 'AACOM') return ViewFormPurchases();
        if(area === 'AAALM') return ViewFormStock();
    }
}

// ** FORM DE PRODUCTOS Y EMPLEADOS (admin area y super admin)