// *** async function getUserData();
// Get user data from server side
async function getUserData() {
    const response = await fetch('/get_user/');
    const data = await response.json();
    return data.user;
}

// Create Singleton Instance
async function getSingleton(){
    const userData = await getUserData(); 
    const userInstance = userSingleton.getInstance(userData);
    const user = userInstance.getUser();
    return user;
}

// *** function getUserType()
// Define the type of user (superuser, admin-area, employee)
const getUserType = (user) => {
    if(user.is_superuser) return 0;
    else if(user.is_area_admin) return 1;
    else return 2;
}

// *** function factoryUserViewHome()
// Call UserFactory and add result to HTML element in home.html depending on user type
const factoryUserViewTable = (user, htmlElement) =>{
    const container = document.getElementById(htmlElement);
    const type = getUserType(user);
    // Views: EmployeeView, AdminAreaView, SuperUserView
    view = new UserViewFactory(new ViewEmployeeTable(), new ViewAdminTable()).create(type);
    container.innerHTML = view.template;
} 

// *** function factoryUserViewForm()
// Call UserFactory and add result to HTML element in form.html depending on user type
const factoryUserViewForm = (user, htmlElement) =>{
    const container = document.getElementById(htmlElement);
    const type = getUserType(user);
    // Views: EmployeeView, AdminAreaView, SuperUserView
    view = new UserViewFactory(new ViewEmployeeForm(), new ViewAdminForm()).create(type);
    container.innerHTML = view.template;
} 

