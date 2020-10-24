from win32com.client import Dispatch

def speak(str):
    speak = Dispatch("SAPI.SpVoice")

    speak.Speak(str)

if __name__ == '__main__':
    speak('Good Evening Shahzaib Rind how are you. Here is me and my name is Robot. and The Owner of the Program is Shahzaib Rind, and Shahzaib is the best guy in the world. hahaha, sorry I am joking. Shahzaib Rind is student of Information Technology in third year and now it’s fifth semester. Bye Bye I am going to charge my battery')
