import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
recognizer=sr.Recognizer()
engine=pyttsx3.init()
newsapi="64ba93b659a04c618d2578334595e267"
def speak(text):
    engine.say(text)
    engine.runAndWait()
def processCommand(c):
     if "open google" in c.lower():
         webbrowser.open("http://google.com")
     elif "open facebook" in c.lower():
         webbrowser.open("http://facebook.com")
     elif "open youtube" in c.lower():
         webbrowser.open("http://youtube.com")
     elif "open linkedin" in c.lower():
         webbrowser.open("http://linkedin.com")
     elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicLibrary.music[song]
        webbrowser.open(link)
     elif "news" in c.lower():
       try:
          r = requests.get(f"https://newsapi.org/v2/everything?q=Pakistan&apiKey={newsapi}")
          print(r.status_code)  # Check the HTTP status code
          print(r.json())       # Print the full response for debugging
          if r.status_code == 200:
             news_data = r.json()
             articles = news_data.get("articles", [])
             if articles:
                speak("Here are the top headlines from Pakistan.")
                for idx, article in enumerate(articles[:10], start=1):  # Fetch top 5 headlines
                    headline = article.get("title", "No title available")
                    print(f"{idx}. {headline}")
                    speak(headline)
             else:
                speak("Sorry, I couldn't find any news articles.")
          else:
            speak(f"Failed to fetch news. Error code: {r.status_code}")
       except Exception as e:
        speak(f"An error occurred while fetching news: {e}")

if __name__=="__main__":
  speak("hi anees! intializing jarvis")
  while True:
             r=sr.Recognizer()
             
             print("recognizing")
             try:
                with sr.Microphone() as source:
                   print("listening......")
                   audio=r.listen(source,timeout=3,phrase_time_limit=2)
                word=r.recognize_google(audio)
                if(word.lower()=="hello"):
                    speak("yes anees boss! how may i help you")
                    with sr.Microphone() as source:
                        print("jarvis active......")
                        audio=r.listen(source)
                        command=r.recognize_google(audio)

                        processCommand(command)
             except sr.UnknownValueError:
                    print("i cannot understand audio")
             except sr.RequestError as e:
                    print("sphinx error;{0}".format(e))

