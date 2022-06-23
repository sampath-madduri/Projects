import pyttsx3
import PyPDF2

def Anyreader(book):
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    print(pages)
    speaker = pyttsx3.init()
    #Enter the page number u want to read
    page = pdfReader.getPage(0)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()

#Give the pdf and the python file that you want to read
book = open('python.pdf', "rb")
result = Anyreader(book)


##with this lines of code you can place the text and speak what ever you want

# import pyttsx3
# speaker = pyttsx3.init()
# speaker.say("Let's make the earth better place ")
# speaker.runAndWait()


