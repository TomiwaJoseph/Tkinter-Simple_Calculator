from tkinter import *

root = Tk()
root.geometry('300x200')
root.resizable(0,0)

class Calculator():
    def __init__(self):
        Label(text='Enter your calculation below',
            font='poppins 14').pack(pady=(20,0))
        self.entry = Entry(font='poppins 10',justify='center',
            width=22)
        self.entry.pack(pady=(5,10))
        Button(command=self.calculate,text='Calculate',fg='#fff',
            bg='green',font='candara 14').pack(pady=(5,5))
        self.output = Label(font='poppins 14')

    def calculate(self):
        self.output.pack(pady=5)
        entry = self.entry.get()
        try:
            output = eval(entry)
            self.output.config(text=f'The result is: {output}',
                fg='green')
        except:
            self.output.config(text='Impossible Calculation',
                fg='red')


if __name__ == '__main__':
    app = Calculator()
    mainloop()