import PyPDF2
import pyttsx3
import tkinter as tk
from tkinter import filedialog

def read_pdf(pdf_path):
    # text-to-speech engine
    engine = pyttsx3.init()

    # PDF location
    with open(pdf_path, 'rb') as pdf_file:
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)
        num_pages = pdf_reader.numPages

        # Convert to speech
        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            engine.setProperty('rate', 150)
            engine.setProperty('volume', 0.9)
            engine.say(text)
            engine.runAndWait()

def select_pdf_path():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])

    if file_path:
        read_pdf(file_path)
    else:
        print("No file selected.")

if __name__ == "__main__":
    select_pdf_path()
