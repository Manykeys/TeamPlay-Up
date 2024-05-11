let findTeam = document.getElementById("findTeam");

if (authorized){
    findTeam.href = "choose";

    let link = document.getElementById("to_authorize");
    link.remove();

    let nickBurg = document.getElementById("nickBurgAuth");
    let nick = document.createElement("h2")
    nick.innerHTML = "ABUBOSLAV";
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
    findTeam.href = "login";
}