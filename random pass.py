from tkinter import*
import random
import string


def generator():
    small_alphabets=string.ascii_lowercase
    capital_alphabets=string.ascii_uppercase
    special_charecters=string.punctuation
    number=string.digits


    all=small_alphabets+capital_alphabets+special_charecters+number
    password_length=int(length_box.get())

    if Choice.get()==1:
           passwordField.insert(0,random.sample(small_alphabets,password_length))

    if Choice.get()==2:
           passwordField.insert(0,random.sample(small_alphabets + capital_alphabets,password_length))
    if Choice.get()==3:
           passwordField.insert(0,random.sample(all,password_length))


    # password=random.sample(all,password_length)
    # passwordField.insert(0,password)
          


root=Tk()
root.config(bg='gray20')
Choice= IntVar()
font=('arial', 13,'bold')
passwordlabel=Label(root, text='password generator',font=('times new roman', 20, 'bold'),bg='gray20', fg='white')
passwordlabel.grid(pady=10)
weakradioButton=Radiobutton(root, text= 'weak',value=1, variable=Choice, font=font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root, text= 'medium',value=2, variable=Choice, font=font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root, text= 'strong',value=3, variable=Choice, font=font)
strongradioButton.grid(pady=5)

lengthlabel=Label(root, text='password length',font=('times new roman', 20, 'bold'),bg='gray20', fg='white')
lengthlabel.grid(pady=5)

length_box=Spinbox(root, from_=2, to=18,width=5, font=font)
length_box.grid(pady=5)

generateButton=Button(root,text='generate',font=font, command=generator)
generateButton.grid(pady=5)

passwordField=Entry(root,width=25,bd=2,font=font)
passwordField.grid(pady=5)



def callback():
      Isum.config(text=Passgen())
      generatorButton=Button(root, text="generate pssword", bd=5,height=2,pady=5)
      generatorButton.grid()
      password=str(callback)
      Isum=Label(root,text="")
      Isum.grid()

root.mainloop()

