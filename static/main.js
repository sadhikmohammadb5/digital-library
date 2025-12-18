console.log("library app loaded");

function Areyousure(){
    if(!confirm("Are you sure you want to logout?")){
        return false;
    }
    else{
        return true;
    }
}   