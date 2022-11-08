from fastapi import FastAPI

app = FastAPI()

db = [
	{
            'name': "Tetris",
            'link': "https://tetris.com/play-tetris/",
            'img': 'https://images.unsplash.com/photo-1646708198974-4c4893e8a2d7?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=687&q=80',
            'description': "Tetris, video game created by Russian designer Alexey Pajitnov in 1985 that allows players to rotate falling blocks strategically to clear levels",
        },
        {
            'name': "Super mario",
            'link': "https://supermario-game.com/",
            'img': 'https://supermarioplay.com/site_image.png',
            'description': "Super Mario Bros.is a platform game.Mario must race through the Mushroom Kingdom and save Princess Toadstool from Bowser. Mario jumps, runs, and walks across each level. The worlds are full of enemies and platforms, and open hole",
        },
        {
            'name': "Pacman",
            'link': "https://freepacman.org/",
            'img': 'https://thelogicalindian.com/h-upload/2021/03/17/1600x960_192284-thelogicalindianfb1000x600-1.jpg',
            'description': "Pac-Man is an action maze chase video game; the player controls the eponymous character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts ",
        },
        {
            'name': "Contra",
            'link': "https://www.retrogames.cz/play_022-NES.php",
            'img': 'https://twistedvoxel.com/wp-content/uploads/2019/05/contra-logo.png',
            'description': "Contra is a run-and-gun shooter video game developed and published by Konami, originally developed as a coin-operated arcade game in 1986",
        },
        {
            'name': "Prince of Persia",
            'link': "https://www.retrogames.cz/play_102-DOS.php",
            'img': 'https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4kvUGP06XxwIDPMDgrganQ/d022a2a43a52926fc81f9c8784d24f1b/media0.jpg',
            'description': "Prince of persia is built around a series of action-adventure games focused on various incarnations of the eponymous Prince, set in ancient and medieval Persia",
        },
        {
            'name': "Street Fighter",
            'link': "https://www.retrogames.cz/play_304-SNES.php",
            'img': 'https://i.ytimg.com/vi/XS5R1g1U_Jw/maxresdefault.jpg',
            'description': "The player controls martial artist Ryu to compete in a worldwide martial arts tournament spanning five countries and 10 opponents",
        },
        {
            'name': "Sonic The HedgeHog",
            'link': "https://www.retrogames.cz/play_117-Genesis.php",
            'img': 'https://i.ytimg.com/vi/WNIOfIGVezc/sddefault.jpg',
            'description': "Sonic is an anthropomorphic blue hedgehog who can run at supersonic speeds and curl into a ball, primarily to attack enemies. In most games, Sonic must race through levels, collecting power-up rings and avoiding obstacles and enemies",
        },
]


@app.get("/")
def home():
    return db
