import datetime
import os
import speech_recognition as sr
import time
import playsound
import pyttsx3
from threading import Thread

# Initialize text-to-speech engine
engine = pyttsx3.init()
engine.setProperty("rate", 150)  # Adjust speech speed if needed

def speak(text):
    """Use pyttsx3 to speak the given text."""
    engine.say(text)
    engine.runAndWait()

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for your command...")
        try:
            audio = recognizer.listen(source)
            print("Recognizing speech...")

            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text.lower()}")

            return text.lower()

        except sr.UnknownValueError:
            print("Sorry, I could not understand the speech.")
            return None
        except sr.RequestError:
            print("Sorry, there was an error with the speech recognition service.")
            return None

def curnt_time():
    return datetime.datetime.now().strftime("%H:%M")

def play_alarm():
    playsound.playsound(r"C:\Users\KASHIF KAMRAN\Desktop\alarm.mp3")  # Update the correct file path

def set_alarm(alarm_time):
    while True:
        current_time = curnt_time()
        if current_time >= alarm_time:
            speak(f"Alarm! It's {alarm_time}.")
            play_alarm()
            break
        time.sleep(10)  # Check every 10 seconds

def voice_activated_alarm():
    speak("Welcome to your voice activated alarm clock!")
    while True:
        command = recognize_speech()
        if command:
            if "what time is it" in command:
                current_time = curnt_time()
                speak(f"The current time is {current_time}")
            elif "set" in command and "alarm" in command:
                try:
                    words = command.split()
                    for i, word in enumerate(words):
                        if ":" in word:  # Find the time in command
                            alarm_time = datetime.datetime.strptime(word, "%H:%M").strftime("%H:%M")
                            speak(f"Setting an alarm for {alarm_time}")
                            Thread(target=set_alarm, args=(alarm_time,)).start()
                            break
                    else:
                        speak("Sorry, I couldn't understand the time. Please try again.")
                except ValueError:
                    speak("Sorry, I couldn't understand the time. Please try again.")
            elif "stop" in command:
                speak("Turning off the alarm clock. Goodbye!")
                break
            else:
                speak("Sorry, I didn't understand that command. Please try again.")

if __name__ == "__main__":
    voice_activated_alarm()
