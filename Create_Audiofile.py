### Create_Audiofile 
### typed in learning by DeAnna 
### 7/27/2022


## Take pdf apart page at a time, read it, send text to 'text to speech', then repeat for each page of pdf file. 

import PyPDF2
pdfReader = PyPDF2.PdfFileReader(open('file.pdf', mode='r+b'))
import pyttsx3
speaker = pyttsx3.init()


## This will repeat for each page. 

for page_num in range(pdfReader.numPages):
    text = pdfReader.getPage(page_num).extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()


## Save audio as mp3 file. 

engine.save_to_file(text, 'audio.mp3')
engine.runAndWait()

