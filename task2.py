import speech_recognition as sr
import webbrowser
import pyttsx3
import os
import sys
import time


pyttsx3.speak(" Howdy  Arvind..I'm Mr. Alex ..")
pyttsx3.speak("Happy to assist you today ..")
print ("Pls let us know your requirements ..", end=' ')
r=sr.Recognizer()

with sr.Microphone() as source:
	print("Pls record your inputs")
	audio = r.listen(source)
	pyttsx3.speak(" We heard your input..please wait while we process it..")
ch = r.recognize_google(audio)
try:
    print("You said: " + r.recognize_google(audio))
except Exception as e:
    print("Error: " + str(e))
			  
if ("date" in ch):
   	webbrowser.open("http://192.168.1.13/cgi-bin/iiec.py?x=date")	
elif "calendar" in ch:
    webbrowser.open("http://192.168.1.13/cgi-bin/iiec.py?x=cal")
elif "media" in ch:
	os.system("start wmplayer")
elif("time" in ch):
	t=time.ctime()
	pyttsx3.speak("Hey Arvind , current time is displayed below")
	print(t)
	
elif ("Youtube" in ch):
    os.system('start chrome "https://www.youtube.com" --kiosk')
	
elif ("Google" in ch):
	pyttsx3.speak("Hey Arvind , here we go...Google search engine is ready for you")
	os.system('start chrome "https://www.google.com" --kiosk')
		
elif ("Facebook" in ch):
  pyttsx3.speak("Hey Arvind , please give us a moment while we open Facebook site for you...")
  os.system('start chrome "https://www.facebook.com" --kiosk') 

elif ("LinkedIn" in ch):
  os.system('start chrome "https://www.linkedin.com/feed/" --kiosk') 

elif ("Amazon" in ch) or ("Console" in ch) or ("amazon" in ch):
  pyttsx3.speak("Hey Arvind , please wait ..we are opening Amazone Web Service console for you in a short while...")
  os.system('start chrome "https://console.aws.amazon.com/console/home?#" --kiosk') 
  
elif ("Flipkart" in ch) or ("flipkart" in ch) :
  pyttsx3.speak("Hey Arvind , please wait ..we are opening Flipkart shopping portal for you in a short while...")
  os.system('start chrome "https://www.flipkart.com/" --kiosk') 
  
elif ("BBC" in ch) or ("News" in ch) :
  pyttsx3.speak("Hey Arvind , here are today's BBC news for you...")
  os.system('start chrome "https://www.bbc.com/" --kiosk')

elif (("run" in ch) and ("calc" in ch)) or ("calculator" in ch):
  os.system("start calc")
elif (("run" in ch) or ("putty" in ch)) or ("Putty" in ch):
  pyttsx3.speak("Hey Arvind , launching Putty application for you ...")
  os.system("start putty")

elif (("start" in ch) and ("notepad" in ch)) or (("Notepad" in ch) or ("Editor" in ch)) :
  pyttsx3.speak("Hey Arvind , launching Notepad editor for you ...")
  os.system("start notepad")
  
elif (("start" in ch) and  ("wordpad" in ch)) or ("Wordpad" in ch) :
  pyttsx3.speak("Hey Arvind , launching Wordpad for you ...")
  os.system("start wordpad")
	  
elif (("start" in ch) and ("Excel" in ch)) or ("Excel" in ch):
  pyttsx3.speak("Hey Arvind , launching Microsoft Excel for you ...")
  os.system("start excel")   
  
elif (("start" in ch) and ("Chrome" in ch)) or ("chrome" in ch):
  pyttsx3.speak("Hey Arvind , launching Google Chrome for you ...")
  os.system("start chrome")
	
elif (("start" in ch) and ("Internet Explorer" in ch)) or ("IE" in ch) or ("ie" in ch) :
  pyttsx3.speak("Hey Arvind , launching Internet Explorer for you to surf ...")
  os.startfile("C:/Program Files/Internet Explorer/iexplore.exe")  
elif (("start" in ch) and ("docker" in ch)):
  webbrowser.open("http://192.168.1.13/drun.html")	
else:
	pyttsx3.speak("Did not understand your choice ..please try again")
