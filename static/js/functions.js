function navigate(url){
    window.location.assign(url);
}

// *** async function getUserData();
// Get user data from server side
async function getUserData() {
    const response = await fetch('/get_user/');
    const data = await response.json();
    console.log(data.user)
    return data.user;
}

// *** async function getSingleton();
// Create Singleton Instance
async function getSingleton(){
    const userData = await getUserData(); 
    const userInstance = userSingleton.getInstance(userData);
    const user = userInstance.getUser();
    return user;
}

// *** function getUserType()
// Define the type of user: superuser, admin-area or employee
const getUserType = (user) => {
    if(user.is_superuser) return 0;
    if(user.is_areaadmin) return 1;
    if(user.is_simplemortal) return 2;
    else return 3;
}

// ----------- Table Factory Views ------------------

    //*** function factoryTableViewProducts()
    //Create Products table depending on the user type
    const factoryTableViewProducts = (user, data) =>{
        // const type = getUserType(user);
        let view;
        if(user.area === 'AA'){
            view = new ViewStockProductsTable(data);
        }
        else if(user.area === 'AAALM' || user.area === 'SADMI'){
            view = new ViewAdminProductsTable(data);
        }
        else{
            view = new ViewEmployeeProductsTable(data);
        }
        return view.template;
    } 

    //*** function factoryTableViewPurchases()
    //Create Purchases table depending on the user type
    const factoryTableViewPurchases = (user, data) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminPurchasesTable(data),
                                new ViewAdminPurchasesTable(data),
                                new ViewEmployeePurchasesTable(data),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewSales()
    //Create Sales table depending on the user type
    const factoryTableViewSales = (user, data) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminSalesTable(data),
                                new ViewAdminSalesTable(data),
                                new ViewEmployeeSalesTable(data),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewStaff()
    //Create Staff table depending on the user type
    const factoryTableViewStaff = (user, data) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewSuperAdminStaffTable(data),
                                new ViewAdminAreaStaffTable(data),
                                new ViewAdminAreaStaffTable(data),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewStock()
    //Create Stock table depending on the user type
    const factoryTableViewStock = (user, data) =>{
        const type = getUserType(user);
        const view = new UserViewFactory(new ViewAdminStockTable(data),
                                new ViewAdminStockTable(data),
                                new ViewEmployeeStockTable(data),
                                ).create(type);
        return view.template;
    } 

// ----------- Form Views ------------------
    
//*** function getFormType()
    //Get Form type: products, stock, sales, purchases, staff, ...
    const getFormType = () =>{
        const url = window.location.href;
        const position = url.search('/form-');
        const type = url.substr(position, url.length);        
        return type;
    }

    //*** function factoryFormView()
    //Create Form depending on the user area
    const factoryFormView = (type) => { 
        return new FormViewFactory().create(type);
    }