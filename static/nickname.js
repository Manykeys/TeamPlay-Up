let nick = document.getElementById("nickname");
let c_start = document.cookie.indexOf("nickname=");
let c_end = document.cookie.indexOf(';', c_start);
nick.innerHTML = document.cookie.substring(c_start + 9, c_end);