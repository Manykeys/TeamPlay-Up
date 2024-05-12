document.addEventListener("DOMContentLoaded", () => {
    let findTeam = document.getElementById("findTeam");

    if (document.cookie.includes('is_authorized=true')){
        findTeam.href = "choose";

        let link = document.getElementById("to_authorize");
        link.remove();

        let nickBurg = document.getElementById("nickBurgAuth");
        let nick = document.createElement("h2");
        let c_start = document.cookie.indexOf("nickname=");
        let c_end = document.cookie.indexOf(';', c_start);
        nick.innerHTML = document.cookie.substring(c_start + 9, c_end);
        nick.className = "nick";
        nickBurg.append(nick)
        let burger = document.createElement("input");
        burger.type = "image";
        burger.className = "menu";
        burger.src = "static/images/burger 3.png";
        nickBurg.append(burger);
    }
    else
    {
        let link = document.getElementById("to_authorize");
        link.style.removeProperty("visibility");
        findTeam.href = "login";
    }
}
);
