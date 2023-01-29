import tkinter

raiz = tkinter.Tk()
raiz.title("Mi programa")

entrada = tkinter.Text(raiz)
entrada.config(width=20,height=10,font=("Verdana",15),padx=10,pady=10,fg="green",selectbackground="lightgrey")
entrada.pack()

raiz.mainloop()