import os
import urllib.request

os.system("sudo apt update && sudo apt install p7zip-full wget nginx git")
os.system("wget https://raw.githubusercontent.com/Invizabel/Scripts/refs/heads/main/Setup/docker_ubuntu.py")
os.system("python3 docker_ubuntu.py")
os.system("wget https://buildbot.libretro.com/stable/1.17.0/emscripten/RetroArch.7z")
os.system("7z x RetroArch.7z")
os.system("git clone https://github.com/ppeccin/javatari.js")
os.system("git clone https://github.com/mitxela/swotGB")
os.system("git clone https://github.com/TimWoelfle/PlainChess")
os.system("sudo mkdir /var/www/html/retroarch")
os.system("sudo mkdir /var/www/html/javatari")
os.system("sudo mkdir /var/www/html/webrcade")
os.system("sudo mkdir /var/www/html/swotgb")
os.system("sudo mkdir /var/www/html/plainchess")
os.system("sudo mkdir /var/www/html/classic")
os.system("sudo cp -r retroarch/* /var/www/html/retroarch")
os.system("sudo cp -r javatari.js/release/stable/5.0/standalone/* /var/www/html/javatari")
os.system("sudo cp -r swotGB/gbjs.htm /var/www/html/swotgb/index.html")
os.system("sudo cp -r PlainChess/* /var/www/html/plainchess")
os.system("wget https://raw.githubusercontent.com/Invizabel/Web-EMU/refs/heads/main/index.html")
os.system("sudo cp index.html /var/www/html/index.html")
os.system("sudo docker run -d --name=webrcade -p 8080:80 -p 8443:443 --restart always webrcade/webrcade:latest")

os.system("mkdir classic")
os.chdir("classic")
if not os.path.exists("assets"):
    os.mkdir("assets")
if not os.path.exists("assets/css"):
    os.mkdir("assets/css")
if not os.path.exists("assets/js"):
    os.mkdir("assets/js")
if not os.path.exists("assets/sounds"):
    os.mkdir("assets/sounds")
if not os.path.exists("assets/textures"):
    os.mkdir("assets/textures")
if not os.path.exists("assets/fonts"):
    os.mkdir("assets/fonts")
if not os.path.exists("assets/textures/previews"):
    os.mkdir("assets/textures/previews")

print("fetching: https://classic.minecraft.net")
response = urllib.request.urlopen("https://classic.minecraft.net").read().decode()
with open("index.html","w") as file:
    file.write(response)

print("fetching: https://classic.minecraft.net/assets/css/style.css?e6201baab01dbc98b4ad")
response = urllib.request.urlopen("https://classic.minecraft.net/assets/css/style.css?e6201baab01dbc98b4ad").read().decode()
with open("assets/css/style.css","w") as file:
    file.write(response)

print("fetching: https://classic.minecraft.net/assets/js/RandomLevelWorker.js")
response = urllib.request.urlopen("https://classic.minecraft.net/assets/js/RandomLevelWorker.js").read().decode()
with open("assets/js/RandomLevelWorker.js","w") as file:
    file.write(response)

print("fetching: https://classic.minecraft.net/assets/js/app.js?e6201baab01dbc98b4ad")
response = urllib.request.urlopen("https://classic.minecraft.net/assets/js/app.js?e6201baab01dbc98b4ad").read().decode()
with open("assets/js/app.js","w") as file:
    file.write(response)

assets_sounds = ["grass1","grass2","grass3","grass4","gravel1","gravel2","gravel3","gravel4","stone1","stone2","stone3","stone4","wood1","wood2","wood3","wood4","calm1","calm2","calm3"]
for i in assets_sounds:
    print(f"fetching: https://classic.minecraft.net/assets/sounds/{i}.mp3")
    response = urllib.request.urlopen(f"https://classic.minecraft.net/assets/sounds/{i}.mp3").read()
    with open(f"assets/sounds/{i}.mp3","wb") as file:
        file.write(response)

assets_textures = ["button_over","button","crosshair","clouds","hotbar_selection","hotbar_bg","grass","dirt","grass_dirt","stone","wood","rock","bedrock","sand","gravel","tree_top","tree_side","lava","rock_gold","rock_bronze","rock_coal","gold","sponge","color0","color1","color2","color3","color4","color5","color6","color7","color8","color9","color10","color11","color12","color13","color14","color15","leaves_opaque","glass","water","bush","red_flower","yellow_flower","red_mushroom","brown_mushroom"]
for i in assets_textures:
    print(f"fetching: https://classic.minecraft.net/assets/textures/{i}.png")
    response = urllib.request.urlopen(f"https://classic.minecraft.net/assets/textures/{i}.png").read()
    with open(f"assets/textures/{i}.png","wb") as file:
        file.write(response)

assets_fonts = ["minecraftfont.woff", "minecraftfont.ttf"]
for i in assets_fonts:
    print(f"fetching: https://classic.minecraft.net/assets/fonts/{i}")
    response = urllib.request.urlopen(f"https://classic.minecraft.net/assets/fonts/{i}").read()
    with open(f"assets/fonts/{i}","wb") as file:
        file.write(response)

textures_previews = ["2","3","4","5","6","8","9","11","12","13","14","15","16","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39"]
for i in textures_previews:
    print(f"fetching: https://classic.minecraft.net/assets/textures/previews/{i}.png")
    response = urllib.request.urlopen(f"https://classic.minecraft.net/assets/textures/previews/{i}.png").read()
    with open(f"assets/textures/previews/{i}.png","wb") as file:
        file.write(response)

os.system("sudo cp -r assets/ /var/www/html/")
os.system("sudo cp -r * /var/www/html/classic/")
