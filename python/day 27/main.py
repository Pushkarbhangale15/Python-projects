import tkinter

window=tkinter.Tk()
window.title("My First GUI Program")
window.minsize(500,300)
#Label
my_label=tkinter.Label(text="This is a label", font=("Arial",24,"bold"))
my_label.grid(column=0,row=0)
#Button
def button_click():
    print("I am clicked")
    new_text=input.get()
    my_label.config(text=new_text)

Button=tkinter.Button(text="Click me", command=button_click)
Button.grid(column=1,row=1)
new_button=tkinter.Button(text="Here!!")
new_button.grid(column=2,row=0)
#Entry
input=tkinter.Entry(width=10)
input.grid(column=3,row=2)







window.mainloop()