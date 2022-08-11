from pygame import mixer

def play_audio(path):
    mixer.init()
    mixer.music.load(path)
    mixer.music.play()

    while True:
        query= input(" ")
        
        if query == "p":
            mixer.music.pause()
        elif query == "r":
            mixer.music.unpause()
        elif query == "q":
            mixer.music.stop()
            break
