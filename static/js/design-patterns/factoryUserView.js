function ViewError(){
    this.template = "<h3>Error: User type invalid</h3>";
}

function UserViewFactory(objectViewEmployee, objectViewAdmin){
    this.create = (type) =>{
        console.log(type);
        if (type === 0) return objectViewAdmin;
        if (type === 1) return objectViewAdmin;
        if (type === 2) return objectViewEmployee;
        if (type != 0 && type != 1 && type != 2) return new ViewError();
    }
}