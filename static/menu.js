let flag = true;
let burger = document.getElementById("burger");
let exit = document.getElementById("exit");
exit.onclick = () =>{
    clearAllCookies();
    window.location.href = "/";
}
burger.onclick = () => {
    let men = document.getElementById("men");
    if (flag){
        men.style.transform = "translateY(200%)";
        flag = false;
    }
    else{
        men.style.transform = "translateY(0)";
        flag = true;
    }
    
}