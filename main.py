import eel
import subprocess

@eel.expose
def play_game():
    try:
        subprocess.run(["python3", "polite_invaders/play.py"])
    except:
        subprocess.run(["python", "polite_invaders"+ "\\" + "play.py"])

@eel.expose
def train_ai():
    try:
        subprocess.run(["python3", "polite_invaders/trainAI.py"])
    except:
        subprocess.run(["python", "polite_invaders"+ "\\"+ "trainAI.py"])

@eel.expose
def test_ai():
    try:
        subprocess.run(["python3", "polite_invaders/testAI.py"])
    except:
        subprocess.run(["python", "polite_invaders" + "\\" + "testAI.py"])

if __name__ == "__main__":
    eel.init("web")
    eel.start("index.html")