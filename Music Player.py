from pygame import mixer


def play_music(file, stopper, player):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()

    while True:
        input_of_user = input()
        if input_of_user == player:
            mixer.music.play()
            if input_of_user == stopper:
                mixer.music.stop()
                break


if __name__ == '__main__':

    print("Welcome To Music Player")
    print("Enter play for play: ")
    print("Enter pause for stop: ")

    while True:
        choose = input("play or pause")
        if choose == 1:
            play_music("water.MP3", 'stop', 'plat')
