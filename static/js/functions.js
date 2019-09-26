// *** function getUser()
// Get user from localSorage and turn into JSON
const getUser = () => { return JSON.parse(localStorage.getItem('user')) };

// *** function factoryUserViewHome()
// Call UserFactory and add result to HTML element in home.html depending on user type
const factoryUserViewTable = (type, htmlElement) =>{
    const container = document.getElementById(htmlElement);
    view = new UserViewFactory(new ViewEmployeeTable(), new ViewAdminTable()).create(type);
    container.innerHTML = view.template;
} 

// *** function factoryUserViewForm()
// Call UserFactory and add result to HTML element in form.html depending on user type
const factoryUserViewForm = (type, htmlElement) =>{
    const container = document.getElementById(htmlElement);
    view = new UserViewFactory(new ViewEmployeeForm(), new ViewAdminForm()).create(type);
    container.innerHTML = view.template;
} 