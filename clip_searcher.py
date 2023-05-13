import pyperclip
import webbrowser

def clip_searcher(word): #function that searches the web for the word
    search_text=f"{word} meaning"
    webbrowser.open(search_text)

def clip_monitor(): #function that monitors the clipboard for a new entry
    previous_clip=pyperclip.paste()
    while(True):
        new_clip=pyperclip.paste()
        
        if new_clip!=previous_clip:
            previous_clip=new_clip
            clip_searcher(new_clip)
            
         
clip_monitor()
