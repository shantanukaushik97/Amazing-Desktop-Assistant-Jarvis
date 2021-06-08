import speech_recognition as sr
import pyttsx3
import os
import pywhatkit
import smtplib
from email.message import EmailMessage
import random
from requests import get
import sys
import datetime
import psutil
import speedtest
import PyPDF2
import wikipedia
import pyautogui
import cv2
import webbrowser
import pyjokes
import json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning Sir!")

    elif hour>=12 and hour<18:
        talk("Good Afternoon Sir!")   

    else:
        talk("Good Evening Sir!")  

    print("I am your Jarvis sir. Your personal AI assistant. Please tell me how may I help you") 
    talk("I am your Jarvis sir . Your personal AI assistant. Please tell me how may I help you")      

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'Jarvis' in command:
                command = command.replace('Jarvis', '')
                print(command)
    except:
        pass
    return command

def pdf_reader():
    book = open('oops.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    talk(f'Total number of pages in this book {pages}')
    print(f'Total number of pages in this book {pages}')
    talk("sir please enter the page number i have to read")
    print("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    talk(text)



def send_email(receiver, subject, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    # Make sure to give app access in your Google account
    server.login('shantanukaushik9761@gmail.com', 'shanyuuu1324')
    email = EmailMessage()
    email['From'] = 'shantanukaushik9761@gmail.com'
    email['To'] = receiver
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)

email_list = {
    'rohit': 'shantanukaushik9761@gmail.com',
    'amit': 'amit360cool@gmail.com',
    'khushboo': 'chaudharykhushboo134@gmail.com',
    'bestie':'geetanjalitewari200@gmail.com',
    'kirti': 'kirtty1905@gmail.com', 
    'sagar': 'sagarminhas2590@gmail.com'   
}

def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=75ddca6231de46ca842e919a76240739'

    main_page = get(main_url).json()

    articles = main_page["articles"]

    head = []
    day = ["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range (len(day)):
        talk(f"today's {day[i]} news is {head[i]}")


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'open youtube' in command:
        talk("Sir , What should I search on youtube")
        ym = take_command()
        webbrowser.open(f"{ym}")
        talk('Opening Youtube for you sir ')
    elif 'date' in command:
        talk('sorry, I have a headache')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'hello' in command:
        talk('Hello Sir. How are you')
    elif 'i am fine' in command:
        talk('Thats good sir what can i do for you')
    elif 'what is this' in command or 'are you fool' in command:
        talk('Sorry Sir.I think you are in the funny mood')
    elif 'latest news' in command:
        talk('Fetching Latest news for you sir ')
        news()
    elif "my location" in command or "where i am" in command :
        talk('Wait Sir Let me Check')
        talk('Sir we are in the Bulanshahr Uttar Pradesh')
    elif 'read pdf' in command:
        talk("Reading pdf sir")
        pdf_reader()

    elif 'my best friend' in command:
        talk('Kirti and Khushboo')
    
    elif 'take screenshot' in command or'take a screenshot'in command:
        talk('Please Sir hold the screen for few seconds . I am taking screenshot')
        screenshot = pyautogui.screenshot()
        screenshot.save("screen.png")
        talk('I am done sir the screenshot is saved in our main folder . Now i am ready for the next command')
    elif 'net speed' in command:
        spt = speedtest.Speedtest()
        dl = spt.download()
        upl = spt.upload()
        talk(f"Sir we have {dl} bit per second downloading speed and {upl} bit per second uploading speed")
    elif 'i feel like i had slept only for 5 minutes' in command:
        talk('I can understand sir . Last night you slept while working . But you slept more than 5 hours and now we have to work')
    elif 'do not disturb me' in command:
        talk('Sir please wake up otherwise i am calling your girlfriend')
    elif 'getting up do not call'in command:
        talk('Thank you sir ')
    elif 'ok wait i am coming' in command:
        talk('Sir where are you going')
    elif 'language' in command:
        talk('Sir i am build on Python by Shantanu Kaushik student of Indian Institute of Information Technology Una')
    elif 'washroom please' in command:
        talk('Sure sir.I thought you are going to sleep again. Please go to washroom')
    elif 'boss' in command:
        talk('Shantanu Kaushik sir')

    elif 'open google' in command:
        talk("Sir , What should I search on google")
        cm = take_command()
        webbrowser.open(f"{cm}")
    elif 'open notepad' in command:
        npath = "C:\\WINDOWS\\system32\\notepad.exe"
        os.startfile(npath)
        talk('Opening Notepad for you sir ')
    elif 'open command prompt' in command:
        os.system('Start Cmd')
        talk('Opening Command Prompt for you sir')
    elif 'how much battery is left' in command:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        talk(f"Sir our system has {percentage} percent battery")
        if percentage >=75:
            talk("Sir we have enough power to continue the work")
        elif percentage>=40 and percentage<=75:
            talk("Sir we should connect our system to the charging point and charge the battery")
        elif percentage<=15 and percentage<=30:
            talk("Sir we don't have enough power to work please charge the battery")
        elif percentage<=15 :
            talk("Sir we have low power . please Charge the system immediately otherwise it will shutdown")
        
    elif 'joke' in command:
        talk("Wait sir i will search joke for you ")
        talk(pyjokes.get_joke())
    elif 'volume up' in command:
        pyautogui.press("volumeup")
    elif 'volume down' in command:
        pyautogui.press("volumedown")
    elif 'mute' in command:
        pyautogui.press("volumemute")
    
    elif 'ip address' in command:
        ip = get('https://api.ipify.org').text
        talk(f"your ip address is {ip}")
    
    elif 'favourite actor' in command:
        talk('shahrukh khan')
    elif 'open camera' in command:
        vid = cv2.VideoCapture(0)
        while (True):
            ret, frame = vid.read()
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vid.release()
        cv2.destroyAllWindows()

    elif 'favourite comedian' in command:
        talk('Jethalal Gada')
    
    elif 'temperature' in command:
        talk('Sir Please tell me the name of the city')
        city_name = take_command()
        talk('Wait sir let me check temperature for you')
        api_key = "921ee4f95cfb8aec20ba1f3268f62b12"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = get(complete_url)
        x = response.json()

        if x["cod"] != "404":
            y = x["main"]
            current_temperature = y["temp"]
            current_pressure = y["pressure"]
            current_humidiy = y["humidity"]
            z = x["weather"]
            weather_description = z[0]["description"]
            talk(" Temperature (in kelvin unit) = " +
                    str(current_temperature) + 
                "\n atmospheric pressure (in hPa unit) = " +
                    str(current_pressure) +
                "\n humidity (in percentage) = " +
                    str(current_humidiy) +
                "\n description = " +
                    str(weather_description))
  
        else:
            talk(" Sorry Sir City Not Found ")
            print(" City Not Found ")
    elif 'random music' in command:
        music_dir = "C:\\Music"
        songs = os.listdir(music_dir)
        rd = random.choice(songs)
        os.startfile(os.path.join(music_dir,rd ))
    elif 'set alarm' in command:
        nn = int (datetime.datetime.now().hour)
        if nn == 9 :
            music_dir = "C:\\Music"
            songs = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, songs[0]))
            talk('Wake Up sir we have to work')
    elif 'something trending' in command:
        music_dir = "C:\\Music"
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir, songs[5]))
    elif 'give me a compliment' in command:
        talk('Your voice is magnificent.')
    elif 'email' in command:
        def get_email_info():
            talk('To Whom you want to send email')
            name = take_command()
            receiver = email_list[name]
            print(receiver)
            talk('What is the subject of your email?')
            subject = take_command()
            talk('Tell me the text in your email')
            message = take_command()
            send_email(receiver, subject, message)
            talk('Sir Your email is sent')
            talk('Do you want to send more email?')
            send_more = take_command()
            if 'yes' in send_more:
                get_email_info()
        
        get_email_info()
        
    elif 'quit' in command:
        print('Thanks for using me sir. Have a good day ')
        talk('Thanks for using me sir. Have a good day ')
        sys.exit()
    else:
        talk('Please say the command again.')

if __name__ == "__main__":
    wishMe()
while True:
    run_alexa()
