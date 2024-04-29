from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from textblob import TextBlob

root=Tk()
root.geometry("700x400")
root.title("Language Translator")
root.config(bg='#D3D3D3')

languages = googletrans.LANGUAGES
language_list = list(languages.values())

def trans_late():
    txt2.delete(1.0, END)
    try:
        from_language_key = next(key for key, value in languages.items() if value == c1.get())
        to_language_key = next(key for key, value in languages.items() if value == c2.get())

        words = TextBlob(txt1.get(1.0, END))
        words = words.translate(from_lang=from_language_key, to=to_language_key)
        txt2.insert(1.0, words)

    except Exception as e:
        messagebox.showerror("Translator", e)

f1 = Frame(root, width=320, height=200, bg='white', bd=5)
f1.place(x=15, y=70)
f2 = Frame(root, width=320, height=200, bg='white', bd=5)
f2.place(x=360, y=70)

txt1=Text(f1,font=('Arial,bold'), width=28, height=8)
txt1.place(x=0,y=0)
txt2=Text(f2,font=('Arial,bold'), width=28, height=8)
txt2.place(x=0,y=0)

c1=ttk.Combobox(root,values=language_list,font=('Arial,bold',12),width=20, state="readonly")
c1.current(1) # set default to English
c1.place(x=60,y=290)

c2=ttk.Combobox(root,values=language_list,font=('Arial,bold',12),width=20, state="readonly")
c2.current(1) # set default to English
c2.place(x=420,y=290)

btn=Button(root,text="Translate",font=('Arial,bold',15),bd=5, bg='#8B8B7A',fg='White',command=trans_late)
btn.place(x=290,y=320)

root.mainloop()