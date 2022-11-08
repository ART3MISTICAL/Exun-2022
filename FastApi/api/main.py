from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ['*']

app.add_middleware(
 CORSMiddleware,
 allow_origins=origins,
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)

db = [
 {
  'name':
  "Tetris",
  'link':
  "https://tetris.com/play-tetris/",
  'img':
  'https://i.ytimg.com/vi/25tt1l23PBc/maxresdefault.jpg',
  'description':
  "Tetris, video game created by Russian designer Alexey Pajitnov in 1985 that allows players to rotate falling blocks strategically to clear levels",
 },
 {
  'name':
  "Super mario",
  'link':
  "https://supermario-game.com/",
  'img':
  'https://supermarioplay.com/site_image.png',
  'description':
  "Super Mario Bros.is a platform game.Mario must race through the Mushroom Kingdom and save Princess Toadstool from Bowser. Mario jumps, runs, and walks across each level. The worlds are full of enemies and platforms, and open hole",
 },
 {
  'name':
  "Pacman",
  'link':
  "https://freepacman.org/",
  'img':
  'https://thelogicalindian.com/h-upload/2021/03/17/1600x960_192284-thelogicalindianfb1000x600-1.jpg',
  'description':
  "Pac-Man is an action maze chase video game; the player controls the eponymous character through an enclosed maze. The objective of the game is to eat all of the dots placed in the maze while avoiding four colored ghosts ",
 },
 {
  'name':
  "Contra",
  'link':
  "https://www.retrogames.cz/play_022-NES.php",
  'img':
  'https://twistedvoxel.com/wp-content/uploads/2019/05/contra-logo.png',
  'description':
  "Contra is a run-and-gun shooter video game developed and published by Konami, originally developed as a coin-operated arcade game in 1986",
 },
 {
  'name':
  "Prince of Persia",
  'link':
  "https://www.retrogames.cz/play_102-DOS.php",
  'img':
  'https://staticctf.akamaized.net/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/4kvUGP06XxwIDPMDgrganQ/d022a2a43a52926fc81f9c8784d24f1b/media0.jpg',
  'description':
  "Prince of persia is built around a series of action-adventure games focused on various incarnations of the eponymous Prince, set in ancient and medieval Persia",
 },
 {
  'name':
  "Street Fighter",
  'link':
  "https://www.retrogames.cz/play_304-SNES.php",
  'img':
  'https://i.ytimg.com/vi/XS5R1g1U_Jw/maxresdefault.jpg',
  'description':
  "The player controls martial artist Ryu to compete in a worldwide martial arts tournament spanning five countries and 10 opponents",
 },
 {
  'name':
  "Sonic The HedgeHog",
  'link':
  "https://www.retrogames.cz/play_117-Genesis.php",
  'img':
  'https://i.ytimg.com/vi/WNIOfIGVezc/sddefault.jpg',
  'description':
  "Sonic is an anthropomorphic blue hedgehog who can run at supersonic speeds and curl into a ball, primarily to attack enemies. In most games, Sonic must race through levels, collecting power-up rings and avoiding obstacles and enemies",
 },
 {
  'name':
  "DOOM(1993)",
  'link':
  "https://www.retrogames.cz/play_414-DOS.php",
  'img':
  'https://cdn.cloudflare.steamstatic.com/steam/apps/2280/header.jpg?t=1663861909',
  'description':
  "Doom is a 1993 science fiction horror-themed first-person shooter (FPS) video game by id Software. It is considered one of the most significant and influential titles in the video game industry, for having ushered in the popularity of the first-person shooter genre.",
 },
 {
  'name':
  "Doom II: Hell on Earth",
  'link':
  "https://www.retrogames.cz/play_462-DOS.php",
  'img':
  'https://images.gog-statics.com/069e485b02c7fdebd492b0c59f27b267c3e65ea8f208af4ca11d904e7223f3c0.jpg',
  'description':
  "Doom II: Hell on Earth is an award winning first-person shooter video game and the second title of id Software's Doom franchise.",
 },
 {
  'name':
  "Donkey Kong",
  'link':
  "https://www.retrogames.cz/play_1067-GameBoy.php",
  'img':
  'https://images.crazygames.com/games/donkey-kong-returns/cover-1630234361535.png?auto=format,compress&q=45&cs=strip&ch=DPR&w=1200&h=630&fit=crop',
  'description':
  "Donkey Kong is a platform game developed in 1994 by Nintendo for the Game Boy handheld video game system, which also contains puzzle elements. Donkey Kong is loosely based on the 1981 arcade game of the same name and its sequel Donkey Kong Jr.",
 },
 {
  'name':
  "Galaga",
  'link':
  "https://www.retrogames.cz/play_018-NES.php",
  'img':
  'https://cdn.cloudflare.steamstatic.com/steam/apps/403430/ss_840d4046749a70d0373c085d100e967ecea2753d.1920x1080.jpg?t=1580375648',
  'description':
  "Galaga is a fixed shooter arcade game developed and published by Namco in Japan and published by Midway in North America in 1981. It is the sequel to Galaxian, released in 1979.",
 },
 {
  'name':
  "Road Rash",
  'link':
  "https://www.retrogames.cz/play_254-Genesis.php",
  'img':
  'https://segaretro.org/images/d/d5/RoadRash_MDTitleScreen.png',
  'description':
  "Road Rash is the name of a motorcycle-racing video game series by Electronic Arts in which the player participates in violent, illegal street races.",
 },
 {
  'name':
  "Sid Meier’s Civilization",
  'link':
  "https://www.retrogames.cz/play_412-DOS.php",
  'img':
  'https://external-preview.redd.it/hEj9-lCr8apZbbWRYqa4XGlo4EYzdy_cUH4swiScCrQ.jpg?width=640&crop=smart&auto=webp&s=f808404b03743c7696abe22f9b10c2f9aef9d202',
  'description':
  "Sid Meier's Civilization is a turn-based strategy '4X'-type strategy video game created by Sid Meier and Bruce Shelley for MicroProse in 1991. The game's objective is to 'Build an empire to stand the test of time",
 },
 {
  'name':
  "Grand Prix Circuit",
  'link':
  "https://www.retrogames.cz/play_413-DOS.php",
  'img':
  'https://www.myabandonware.com/media/screenshots/g/grand-prix-circuit-ga/grand-prix-circuit_1.png',
  'description':
  "Grand Prix Circuit is a racing video game developed by Distinctive Software and published by Accolade for MS-DOS com­pa­tib­le operating systems in 1988. ",
 },
 {
  'name':
  "Mortal Kombat II",
  'link':
  "https://www.retrogames.cz/play_310-Genesis.php",
  'img':
  'https://oyster.ignimgs.com/mediawiki/apis.ign.com/mortal-kombat-2/a/a2/GameplayScreenShot.jpg',
  'description':
  "Mortal Kombat II (commonly abbreviated as MKII) is a competitive fighting game originally produced by Midway Games for the arcades in 1993. ",
 },
 {
  'name':
  "Street Fighter II Turbo: Hyper Fighting",
  'link':
  "https://www.retrogames.cz/play_1133-SNES.php",
  'img':
  'https://i.ytimg.com/vi/A6fs7qIXACY/maxresdefault.jpg',
  'description':
  "Street Fighter II Turbo: Hyper Fighting is a competitive fighting game released for the arcade by Capcom in 1992. It is the third game in the Street Fighter II sub-series of Street Fighter games following Street Fighter II: Champion Edition.",
 },
 {
  'name':
  "Baseball[NES](1983)",
  'link':
  "https://www.retrogames.cz/play_057-NES.php",
  'img':
  'https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/virtual_console_wii_u_7/SI_WiiUVC_Baseball_image1600w.jpg',
  'description':
  "Baseball is a video game made by Nintendo in 1983 for the Nintendo Family Computer, making it one of the first games released for the Famicom",
 },
 {
  'name':
  "Donkey Kong Country",
  'link':
  "https://www.retrogames.cz/play_289-SNES.php",
  'img':
  'https://i.ytimg.com/vi/_4EjGXRDOH0/maxresdefault.jpg',
  'description':
  "Donkey Kong Country is a 1994 platforming video game developed by Rare and published by Nintendo for the Super Nintendo Entertainment System. It was first released on November 21, 1994 in North America.",
 },
 {
  'name':
  "Chip ’N Dale: Rescue Rangers",
  'link':
  "https://www.retrogames.cz/play_198-NES.php",
  'img':
  'https://i.ytimg.com/vi/cprxEhyt6tc/maxresdefault.jpg',
  'description':
  "Chip 'n Dale Rescue Rangers is a platform game featuring single and 2-player cooperative modes, allowing players to choose which levels to access via a map of various locations throughout the city, in a similar format to other Capcom games such as Bionic Commando.",
 },
 {
  'name':
  "Prince of Persia 2: The Shadow & The Flame",
  'link':
  "https://www.retrogames.cz/play_260-DOS.php",
  'img':
  'https://www.myabandonware.com/media/screenshots/p/prince-of-persia-2-the-shadow-the-flame-3u9/prince-of-persia-2-the-shadow-the-flame_7.png',
  'description':
  "Similar to the first Prince of Persia, In the sequel, the character explores various deadly areas by running, jumping, crawling, avoiding traps, solving puzzles and drinking magic potions. Prince of Persia 2 is, however, more combat-heavy than its predecessor.",
 },
 {
  'name':
  "SimCity 2000",
  'link':
  "https://www.retrogames.cz/play_473-DOS.php",
  'img':
  'https://i.ytimg.com/vi/fn9nN5NxOK8/maxresdefault.jpg',
  'description':
  "SimCity 2000 (SC2K) is a city-building simulation video game and the second installment in the SimCity series. SimCity 2000 was first released by Maxis in 1994 for computers running Apple Macintosh Operating System. It was later released on the Amiga, DOS & Microsoft Windows, followed by a release for OS/2.",
 },
 {
  'name':
  "Teenage Mutant Ninja Turtles(1989)",
  'link':
  "https://www.retrogames.cz/play_015-NES.php",
  'img':
  'https://i.ytimg.com/vi/7P3I0DFlBRs/mqdefault.jpg',
  'description':
  "Teenage Mutant Ninja Turtles, originally released as Fierce Turtle Ninja Legend in Japan and later as Teenage Mutant Hero Turtles in Europe, is a 1989 platform game for the Famicom/NES.",
 },
 {
  'name':
  "Donkey Kong Country 2: Diddy’s Kong Quest",
  'link':
  "https://www.retrogames.cz/play_785-SNES.php",
  'img':
  'https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/game_boy_advance_7/SI_GBA_DonkeyKongCountry2_image1600w.jpg',
  'description':
  "Donkey Kong Country 2: Diddy's Kong Quest, commonly abbreviated to DKC2, is a 1995 adventure platforming video game developed by Rare and published by Nintendo for the Super Nintendo Entertainment System.",
 },
 {
  'name':
  "Street Fighter Alpha 2",
  'link':
  "https://www.retrogames.cz/play_1142-SNES.php",
  'img':
  'https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/virtual_console_wii_u_7/SI_WiiUVC_StreetFighterAlpha2_image1600w.jpg',
  'description':
  "Street Fighter Alpha 2, known as Street Fighter Zero 2 in Japan/Asia and South America, is a 1996 fighting game originally released for the CPS II arcade hardware by Capcom. The game is both a sequel and a remake to the previous year's Street Fighter Alpha.",
 },
 {
  'name':
  "Contra Force",
  'link':
  "https://www.retrogames.cz/play_281-NES.php",
  'img':
  'https://i.ytimg.com/vi/EGPiQov78Fs/maxresdefault.jpg',
  'description':
  "Contra Force is an action shooting game released by Konami for the Nintendo Entertainment System in 1992 exclusively in North America. It is a spinoff of the Contra series, being the third game in the series released for the NES following the original Contra and Super C.",
 },
 {
  'name':
  "Pong-Atari(1972)",
  'link':
  "https://www.retrogames.cz/play_530-DOS.php",
  'img':
  'https://i.ytimg.com/vi/-vbGBlxVxcQ/maxresdefault.jpg',
  'description':
  "Pong (marketed as PONG) is one of the earliest arcade video games; it is a tennis sports game featuring simple two-dimensional graphics. While other arcade video games such as Computer Space came before it, Pong was one of the first video games to reach mainstream popularity."
 },
 {
  'name':
  "Space Invaders(1978)",
  'link':
  "https://www.retrogames.cz/play_016-Atari2600.php",
  'img':
  'https://ichef.bbci.co.uk/images/ic/1920x1080/p0738203.jpg',
  'description':
  "Space Invaders is an arcade video game developed by Tomohiro Nishikado and released in 1978. Space Invaders is one of the earliest shooting games and the aim is to defeat waves of aliens with a laser cannon to earn as many points as possible.",
 },
 {
  'name':
  "Formula One Grand Prix",
  'link':
  "https://www.retrogames.cz/play_454-DOS.php",
  'img':
  'https://i.ytimg.com/vi/U4fC9CAjJPE/maxresdefault.jpg',
  'description':
  "Formula One Grand Prix (known as World Circuit in the United States) is a racing simulator released in 1992 by MicroProse for the Atari ST, Amiga and PC created by game designer Geoff Crammond.",
 },
 {
  'name':
  "Star Wars: The Empire Strikes Back",
  'link':
  "https://www.retrogames.cz/play_813-Atari2600.php",
  'img':
  'https://www.giantbomb.com/a/uploads/scale_medium/8/87790/1787599-box_sswtesb.png',
  'description':
  "Star Wars: The Empire Strikes Back is a scrolling shooter video game published by Parker Brothers in 1982 for the Atari 2600. It was the first licensed Star Wars video game.",
 },
 {
  'name':
  "Galaxian(1979)",
  'link':
  "https://www.retrogames.cz/play_019-Atari2600.php",
  'img':
  'https://i.ytimg.com/vi/YRk_ulZ8MMY/maxresdefault.jpg',
  'description':
  "Galaxian is an arcade game that was developed by Namco in October 1979.  A fixed shooter game in which the player controls a spaceship at the bottom of the screen, and shoots enemies descending in various direction.",
 },
]


@app.get("/")
def home():
	return db


uvicorn.run(app, host="0.0.0.0", port="8080")
