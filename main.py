import eel
import subprocess

@eel.expose
def play_game():
    subprocess.run(["python3.7", "polite_invaders/play.py"])

@eel.expose
def train_ai():
    subprocess.run(["python3.7", "polite_invaders/trainAI.py"])

@eel.expose
def test_ai():
    subprocess.run(["python3.7", "polite_invaders/testAI.py"])

if __name__ == "__main__":
    eel.init("web")
    eel.start("index.html")