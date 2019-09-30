// *** async function getUserData();
// Get user data from server side
async function getUserData() {
    const response = await fetch('/get_user/');
    const data = await response.json();
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
    if(user.is_area_admin) return 1;
    if(user.is_simplemortal) return 2;
    else return 3;
}

// ----------- Table Factory Views ------------------

    //*** function factoryTableViewProducts()
    //Create Products table depending on the user type
    const factoryTableViewProducts = (user) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminProductsTable(),
                                new ViewAdminProductsTable(),
                                new ViewEmployeeProductsTable(),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewPurchases()
    //Create Purchases table depending on the user type
    const factoryTableViewPurchases = (user) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminPurchasesTable(),
                                new ViewAdminPurchasesTable(),
                                new ViewEmployeePurchasesTable(),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewSales()
    //Create Sales table depending on the user type
    const factoryTableViewSales = (user) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewAdminSalesTable(),
                                new ViewAdminSalesTable(),
                                new ViewEmployeeSalesTable(),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewStaff()
    //Create Staff table depending on the user type
    const factoryTableViewStaff = (user) =>{
        const type = getUserType(user);
        view = new UserViewFactory(new ViewSuperAdminStaffTable(),
                                new ViewAdminAreaStaffTable(),
                                new ViewAdminAreaStaffTable(),
                                ).create(type);
        return view.template;
    } 

    //*** function factoryTableViewStock()
    //Create Stock table depending on the user type
    const factoryTableViewStock = (user) =>{
        const type = getUserType(user);
        const view = new UserViewFactory(new ViewAdminStockTable(),
                                new ViewAdminStockTable(),
                                new ViewEmployeeStockTable(),
                                ).create(type);
        return view.template;
    } 

// ----------- Form Views ------------------

    //*** function factoryFormView()
    //Create Form depending on the user area
    const factoryFormView = (user) => { 
        return new FormViewFactory().create(user.area);
    }

    //*** function factoryFormProductsView()
    //Create Products Form depending on the user area
    const factoryFormProductsView = (user) => { 
        return new FormProductsViewFactory().create(user.area);
    }

