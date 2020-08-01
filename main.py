import eel
import subprocess
import sys

@eel.expose
def play_game():
    if (sys.platform).startswith("win"):
        subprocess.run(["python", "polite_invaders"+ "\\" + "play.py"])
    else:
        subprocess.run(["python3", "polite_invaders/play.py"])
       

@eel.expose
def train_ai():
    if (sys.platform).startswith("win"):
        subprocess.run(["python", "polite_invaders"+ "\\"+ "trainAI.py"])    
    else:
        subprocess.run(["python3", "polite_invaders/trainAI.py"])
        

@eel.expose
def test_ai():
    if (sys.platform).startswith("win"):
        subprocess.run(["python", "polite_invaders" + "\\" + "testAI.py"])    
    else:
        subprocess.run(["python3", "polite_invaders/testAI.py"])

@eel.expose
def play_music():
    if (sys.platform).startswith("win"):
        subprocess.run(["python", "Music" + "\\" + "music_player.py"])    
    else:
        subprocess.run(["python3", "Music/music_player.py"])

        

if __name__ == "__main__":
    eel.init("web")
    eel.start("index.html")