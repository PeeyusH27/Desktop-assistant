import pyttsx3 #Python text to speech module x3 means for python 3 n above
import datetime #extract date and time, also calander functions
import speech_recognition as sr #speech recog module helps in taking voice input which is converted to text by PYTTSx3
import wikipedia #information about anything from wiki
import webbrowser #open any specific ulr to search anything with voice commands
import os 
import subprocess#admin control of ur system basically helps in shutdown, restart etc
import shutil


engine = pyttsx3.init('sapi5') #sapi5 is Microsoft Speech API (SAPI5) is the technology for voice recognition and synthesis provided by Microsoft
voices = engine.getProperty('voices') #will extract the available voices you have in ur system
engine.setProperty('voices', voices[0].id) #choose the voice u want to use and set it with its id
AssistantName = ("Matrix")

def usrname():
    speak("What should i call you sir")
    print("What should i call you sir")
    uname = takecommand()
    speak(f"Welcome Mister {uname}")
    columns = shutil.get_terminal_size().columns

def speak(audio):
    engine.say(audio) #speak function output from speaker
    engine.runAndWait() #raise RuntimeError: When the loop is already running

def wishme(): #first func to excecute when the program runs
    '''recognizes time and wish according to given time format'''
    hour = int(datetime.datetime.now().hour) #Greeting depending upon current time
    if hour >= 0 and hour<12:
        speak("Good morning")
        print("Good morning")
    elif hour>=12 and hour<18:
        speak("Good afternoon")
        print("Good afternoon")
    else:
        speak("Good evening")
        print("Good evening")
    print(f"I am {AssistantName} your desktop assistant, how can i help you?")
    speak(f"I am {AssistantName} your desktop assistant, how can i help you?")



def takecommand(): #voice input function
    '''Take microphone input and returns string as output'''
    r = sr.Recognizer() 
    with sr.Microphone() as source: #uses microphone as source by using sr recognizer function
        print("Listening...") #to know the program is working(listening to commands)
        r.pause_threshold = 0.5 #u can increase or decrease the time for what the program will take user input
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in') #query is what is used to trigger the program when the string in query matches the voice command only then the desired function excecutes
        print(f"You asked for: {query}\n") #returns Text form of voice command
    except Exception as e: #if user said nothing in the given time or voice was not recognizable
        print("Unable to recognize.")
        return "None"
    return query

def tellDay(): 
      
    # This function is for telling the 
    # day of the week 
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number  
    # that will help us in telling the day 
    Day_dict = {1: 'Monday', 2: 'Tuesday',  
                3: 'Wednesday', 4: 'Thursday',  
                5: 'Friday', 6: 'Saturday', 
                7: 'Sunday'} 
      
    if day in Day_dict.keys(): 
        day_of_the_week = Day_dict[day] 
        print(day_of_the_week) 
        speak("The day is " + day_of_the_week)

if __name__ == "__main__":
    clear = lambda: os.system('cls')

    # This Function will clean any
    # command before execution of this python file
    clear() #clear previous queries commands
    usrname()
    wishme() #GREETS before starting the loop(only once when the program is started)


    while True:
        query = takecommand().lower() #converts query to lower to match with google recognizer
    #recognizes speech to build logic for excecuting task based on query
        if 'wikipedia' in query:
            speak('Searching wikipedia....')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences = 3)
                speak("According to Wikipedia")
                print("According to wikipedia:")
                print(results)
                speak(results)
            except Exception as e:
                speak("Unable to find information, try something else")
                print("Unable to find information, try something else")
                continue
            
        elif 'how are you' in query:
            speak("I am fine, Thank you")
            speak("How are you, Sir")

        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")

        elif "what can you do" in query:
            print("I can help you out in performing usual tasks by voice commands.")
            print("you can ask for: ") 
            print("Opening applications, Searching information from web and many more..")

        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            AssistantName = takecommand()
            speak(f"name changed to {AssistantName}")
            print(f"name changed to {AssistantName}")

        elif  "search for" in query:
            search_term = query.split("for")[-1]
            url = (f"https://google.com/search?q={search_term}")
            query = query.replace("search", "")
            webbrowser.get().open(url)
            speak("Here are the results.")

        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location + "")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 
            print("opening youtube")
            speak("opening youtube")

        elif 'open google' in query:
            url = "www.google.co.in"
            chrome_path = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe %s'
            webbrowser.get(chrome_path).open(url)
            print("opening google")
            speak("opening google")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")
            print("opening whatsapp")
            speak("you better be studying")

        elif 'open code' in query:
            codePath = "C:\\Users\\peeyu\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
            speak("opening visual studio code")
            print("opening visual studio code")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\peeyu\\Downloads\\songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0])) #you can change path and edit the id so as to ask which song should be played

        elif 'empty recycle bin' in query:
            winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
            speak("Recycle Bin Recycled")

        elif 'play movie' in query:
            video_dir = 'C:\\Users\\peeyu\\Downloads\\MOVIES\\tamasha'
            movies = os.listdir(video_dir)
            print(movies)
            os.startfile(os.path.join(video_dir, movies[0]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
            print(f"The time is {strTime}")

        elif 'what day' in query:
            print(tellDay())
            speak(tellDay())
            continue

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takecommand())
            time.sleep(a)
            print(a)
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takecommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takecommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)

        elif "show note" in query:
            speak("Showing Notes")
            file = open("jarvis.txt", "r")
            print(file.read())
            speak(file.read(6)) 
             
        elif 'exit' in query: #stop the loop
            speak("Have a good day.")
            print("Have a good day.")
            exit()
