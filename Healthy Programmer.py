# Healthy Programmer
# 9:00 to 5:00pm
# Water - Water.Mp3 (3.5 Liters) - Drank - Log Every 40 Min
# Eyes - eyes.Mp3 Every 30 Min - EyDone - Log Every 30 Min
# Physical Activity - physical.Mp3 Every 45 Min - ExDone - Log
# Rules
# Pygame Module to Play Audio

from pygame import mixer
from datetime import datetime
from time import time

def musicloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break

def log_now(msg):
    with open("mylogs.txt", "a") as f:
        f.write(f"{msg} {datetime.now()} \n")


if __name__ == '__main__':
    # musicloop("water.mp3", "stop")
    init_water = time()
    init_eyes = time()
    init_excer = time()
    watersecs = 40*60
    exsecs = 30*60
    eyessecs = 45 * 60

    while True:
        if time() - init_water > watersecs:
            print("Water Drinking time, Enter 'done' to stop' the Alarm")
            musicloop("water.MP3", "done")
            init_water = time()
            log_now("Drank Water at: ")

            if time() - init_eyes > eyessecs:
                print("Eyes Excercise Time , Enter 'done' to stop the Alarm")
                musicloop("eyes.mp3", "done")
                init_eyes = time()
                log_now("Eyes Relaxed Done at: ")

                if time() - init_excer > exsecs:
                    print("Physical Excersice time starts, Enter 'done' to stop")
                    musicloop("excer.mp3", "done")
                    init_excer = time()
                    log_now("Physical Done at: ")
