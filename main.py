from tkinter import * 
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"

window=Tk()
window.configure(bg=BACKGROUND_COLOR,padx=50,pady=50)
window.minsize(width=900,height=626)

def show_translation():
    global on,h_word
    canvas.itemconfig(word,text=h_word,fill="black")
    canvas.itemconfig(card,image=img_card_back)
    canvas.itemconfig(title,text="עברית")
    on=True
def fun():
    global on,h_word,e_word
    if not on:
        return
    on=False
    global index
    
    index=random.randint(0,len(dict_data["english"])-1)
    print(index)
    print(data.iloc[index]["english"])
    e_word=dict_data["english"][index]
    h_word=dict_data["hebrew"][index]
    canvas.itemconfig(word,text=e_word)
    # canvas.itemconfig(word,text=dict_data["english"][index])
    canvas.itemconfig(card,image=img_card_front)
    canvas.itemconfig(title,text="english")
    window.after(3000,show_translation)
def delete_word():
    global on,h_word,e_word
    if not on:
        return
    # print(e_word," ",h_word)
    # dict_data["english"].remove(e_word)
    # dict_data["english"].remove(dict_data["english"][index])
    # dict_data["hebrew"].remove(h_word)
    # dict_data["hebrew"].remove(dict_data["hebrew"][index])

    new_file=pandas.DataFrame(dict_data)
    new_file.drop(index=index)
    new_file.to_csv('data/words_to_learn.csv',index=True)
    
    fun()

on=True
img_v=PhotoImage(file='images/right.png')
img_x=PhotoImage(file='images/wrong.png')
img_card_front=PhotoImage(file='images/card_front.png')
img_card_back=PhotoImage(file='images/card_back.png')
canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card=canvas.create_image(400,270,image = img_card_front)
title=canvas.create_text(400,150,text="English",font= ("Ariel",40,"italic") )
word=canvas.create_text(400,264,text="trouve",font= ("Ariel",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)
btn_right=Button(image=img_v,command=delete_word)
btn_worng=Button(image=img_x,command=fun)
btn_right.grid(row=1,column=1)
btn_worng.grid(row=1,column=0)
try:
    data=pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    data=pandas.read_csv("./data/data.csv")


english_data=data["english"].to_list()
hebrew_data=data["hebrew"].to_list()
dict_data={"english":english_data,"hebrew":hebrew_data}
fun()
window.mainloop()
