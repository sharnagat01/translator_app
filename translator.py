from tkinter import  *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

mycolor ='#292075'
mycolor2 = '#00b5ef'
root = Tk()
root.geometry('500x400')
root.title('Language Translator')
p1 = PhotoImage(file = '1.png')
root.iconphoto(False,p1)
root.resizable(False,False)
root.configure(bg= mycolor)

lang_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az', 'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca', 'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw', 'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en', 'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy', 'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu', 'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn', 'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it', 'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko', 'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv', 'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms', 'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn', 'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps', 'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru', 'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd', 'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su', 'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th', 'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi', 'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}

def tt(event=None):
    try:
        word = TextBlob(varname.get())
        lang = word.detect_language()
        lang_to_dict = languages.get()
        lang_to = lang_dict[lang_to_dict]
        word = word.translate(from_lang=lang, to=lang_to)
        label3.configure(text=word)
        varname1.set(word)
    except:
        varname1.set('Try another Keyword')
def mainexit():
    rr = messagebox.askyesnocancel('Notification','Do you want to  Exit Translator',parent=root)
    if(rr == True):
        root.destroy()
def onenter(e):
    data1['bg'] = 'springgreen'
def onleave(e):
    data1['bg'] = 'white'
def onenter1(e):
    data2['bg'] = 'springgreen'
def onleave1(e):
    data2['bg'] = 'white'
def onenter2(e):
    bttn1['bg'] = 'springgreen'
def onleave2(e):
    bttn1['bg'] = 'white'
def onenter3(e):
    bttn2['bg'] = 'springgreen'
def onleave3(e):
    bttn2['bg'] = 'white'










languages = StringVar()
font_box = Combobox(root,width = 30, textvariable =languages,state ='readonly')
font_box['values']= [e for e in lang_dict.keys()]
font_box.current(37)
font_box.place(x=300,y=0)


varname = StringVar()
data1 = Entry(root,width=30,textvariable=varname,font=('times',10,'italic bold'))
data1.place(x=150,y=40)
varname1 = StringVar()
data2 = Entry(root,width=30,textvariable=varname1,font=('times',10,'italic bold'))
data2.place(x=150,y=100)

label1 = Label(root,text='Enter Words :',font= ('times',10,'italic bold'),bg=mycolor2)
label1.place(x=5,y=40)
label2 = Label(root,text='Translated:',font= ('times',10,'italic bold'),bg=mycolor2)
label2.place(x=5,y=100)
label3 = Label(root,text='',font= ('times',10,'italic bold'),bg=mycolor2)
label3.place(x=10,y=250)

imgbt1 = PhotoImage(file='click.png')
imgbt2 = PhotoImage(file='exit.png')
imgbt1 = imgbt1.subsample(2,2)
imgbt2 = imgbt2.subsample(2,2)

bttn1 = Button(root,text='Translate',bd=10,bg='white', activebackground ='red',width=100,font= ('times',10,'italic bold'),
               image =imgbt1,compound=RIGHT,command = tt)
bttn1.place(x=70,y=170)
bttn2 = Button(root,text='Exit',bd=10,bg='white', activebackground ='red',width=100,font= ('times',10,'italic bold'),
               image =imgbt2,compound=RIGHT,command = mainexit)
bttn2.place(x=280,y=170)
root.bind('<Return>',tt)


data1.bind('<Enter>', onenter)
data1.bind('<Leave>', onleave)

data2.bind('<Enter>', onenter1)
data2.bind('<Leave>', onleave1)

bttn1.bind('<Enter>', onenter2)
bttn1.bind('<Leave>', onleave2)

bttn2.bind('<Enter>', onenter3)
bttn2.bind('<Leave>', onleave3)






root.mainloop()
