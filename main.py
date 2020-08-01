import eel
import subprocess

@eel.expose
def play_game():
    print(subprocess.run(["python3.7", "polite_invaders/play.py"]))

if __name__ == "__main__":
    eel.init("web")
    eel.start("index.html")