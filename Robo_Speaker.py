import pyttsx3

if __name__ == '__main__':
    text_to_speak = pyttsx3.init()
    while(True):
        word = input("Enter your comment: ")
        if word == 'q':
            text_to_speak.say("Bye bye friends")
            text_to_speak.runAndWait()
            break
        text_to_speak.say(word)
        text_to_speak.runAndWait()