## ⏰ Voice-Activated Alarm System  

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Speech Recognition](https://img.shields.io/badge/Speech_Recognition-GoogleAPI-green)  

### 📌 Overview  
The **Voice-Activated Alarm System** is a Python-based program that lets users set alarms using voice commands. It uses **speech recognition** to understand user instructions and triggers an alarm at the specified time.  

### 🚀 Features  
- ✅ Voice-based interaction for setting alarms  
- ✅ Real-time speech recognition using Google Speech API  
- ✅ Text-to-speech response using pyttsx3  
- ✅ Plays an alarm sound at the scheduled time  
- ✅ Retrieves and announces the current time  

### 🛠️ Technologies Used  
- **Python**  
- **SpeechRecognition** (Google Speech API)  
- **Pyttsx3** (Text-to-speech)  
- **Playsound** (Alarm sound playback)  
- **Threading** (For parallel execution)  

### 📂 Installation & Setup  
1️⃣ Clone this repository or download the script:  
```bash
git clone https://github.com/KxshxfKxmrxn/voice-activated-alarm.git
cd voice-activated-alarm
```  
2️⃣ Install required dependencies:  
```bash
pip install speechrecognition pyttsx3 playsound
```  
3️⃣ Place your **alarm.mp3** file in the correct directory and update its path in the script.  

4️⃣ Run the script:  
```bash
python voice_activated_alarm.py
```  

### 🎤 Usage Instructions  
🔹 Run the script and speak the following commands:  
- **"What time is it?"** → Announces the current time  
- **"Set alarm for HH:MM"** → Sets an alarm at the given time  
- **"Stop"** → Exits the program  

### 📸 Preview  
```
Listening for your command...
Recognizing speech...
Recognized Text: set alarm for 07:30
Setting an alarm for 07:30
```

### 🛠️ Future Improvements  
- ✨ Adding a GUI for better user experience  
- ✨ Enhancing speech recognition accuracy  
- ✨ Integrating voice assistant support  

