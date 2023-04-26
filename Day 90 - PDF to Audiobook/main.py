import pyttsx3 as tts
import PyPDF3
import pdfplumber

file = "lorem.pdf"

book = open(file, 'rb')
pdfReader = PyPDF3.PdfFileReader(book)

pages = pdfReader.numPages

finalText = ''
with pdfplumber.open(file) as pdf:
    for i in range(0, pages):
        page = pdf.pages[i]
        text = page.extract_text()
        finalText += text

# If you want to convert the text into audio and save it into a new file,
# engine = tts.init()
# engine.save_to_file(finalText, 'lorem.mp3')
# engine.runAndWait()

# If you don't want to save the audiobook and want to recite the PDF file
engine = tts.init()
engine.say(finalText)
engine.runAndWait()


