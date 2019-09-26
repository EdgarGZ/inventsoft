let userSingleton = (function(){
    let userInstance;
    const create = (userObject) => {
        console.log("Creating new instance");
        let user = userObject;
        let getUser = () => {return user}
        return{
            getUser: getUser
        }
    }
    return {
        getInstance: (userObject) => {
            console.log("Getting instance");
            if(!userInstance) userInstance = create(userObject);
            return userInstance;
        },
        removeInstance: () => {
            if(userInstance) userInstance = null;
            return userInstance;
        }
    }
})();


var userInstance;
var user;

let setSingletonInstance = (userData) => { 
    // userInstance = userSingleton.getInstance(userData);
    // user = userInstance.getUser();
    if(!user){
        console.log("Creating user");
        user = 5;
    }
    else{
        console.log("User has been created");
    }
    return user;
}
let getSingletonInstance = () => { 
    return setSingletonInstance('');
}