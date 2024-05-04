let games = ["Dota 2", "dota2", "Counter-Strike 2", "cs2", "World of Tanks", "wot", "PUBG", "pubg",
 "APEX LEGENDS", "apex", "HeartStone", "heartstone", "Valorant", "valorant", "Overwatch", "overwatch"];
let divchik = document.getElementById('games');
for (let i = 0; i < games.length; i += 2){
    let game = document.createElement('div');
    game.className = "game";
    let gameImg = document.createElement('img');
    gameImg.src = `static/choose_images/${games[i]}.png`;
    gameImg.className = "gameImage";
    game.append(gameImg);
    let gameName = document.createElement('p');
    gameName.innerHTML = games[i];
    gameName.className = "gameName";
    game.append(gameName);
    let href = document.createElement('a');
    href.innerHTML = "Собрать команду";
    href.href = `${games[i + 1]}`;
    href.className = "gatherTeam";
    game.append(href);
    divchik.append(game);
}
